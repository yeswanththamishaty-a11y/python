
import math

def calculate_charge(weight, length, width, height, zone, urgency, restricted):
    # Calculate volumetric weight (in cm, divided by 5000)
    volumetric_weight = (length * width * height) / 5000
    chargeable_weight = max(weight, volumetric_weight)

    # Round up to the next 0.5 kg
    chargeable_weight = math.ceil(chargeable_weight * 2) / 2

    # Distance zone charges
    zone_rates = {
        "local": 30,
        "regional": 50,
        "national": 80
    }

    if zone not in zone_rates:
        return None

    base_charge = zone_rates[zone]
    weight_charge = chargeable_weight * 20

    # Urgency charges
    urgency_rates = {
        "standard": 0,
        "express": 50,
        "same-day": 100
    }

    if urgency not in urgency_rates:
        return None

    # Restrictions: restricted items require special handling
    if restricted:
        handling_charge = 40
    else:
        handling_charge = 0

    total = (
        base_charge
        + weight_charge
        + urgency_rates[urgency]
        + handling_charge
    )

    return total, chargeable_weight


def optimize_courier(weight, length, width, height,
                     zone, urgency, restricted):

    services = {
        "FastCourier": {
            "max_weight": 20,
            "max_volume": 100000,
            "restricted": False
        },
        "SafeExpress": {
            "max_weight": 30,
            "max_volume": 150000,
            "restricted": True
        },
        "BudgetDelivery": {
            "max_weight": 10,
            "max_volume": 50000,
            "restricted": False
        }
    }

    volume = length * width * height
    eligible = []

    for name, service in services.items():
        if weight > service["max_weight"]:
            continue

        if volume > service["max_volume"]:
            continue

        if restricted and not service["restricted"]:
            continue

        result = calculate_charge(
            weight, length, width, height,
            zone, urgency, restricted
        )

        if result is not None:
            charge, chargeable_weight = result
            eligible.append(
                (name, charge, chargeable_weight)
            )

    print("\n--- Courier Charge Comparison ---")

    if not eligible:
        print("No eligible courier service found.")
        return

    for name, charge, cw in eligible:
        print(
            f"{name}: Rs.{charge:.2f} "
            f"(Chargeable weight: {cw:.1f} kg)"
        )

    best = min(eligible, key=lambda item: item[1])

    print("\n--- Best Courier Option ---")
    print("Service:", best[0])
    print(f"Minimum Charge: Rs.{best[1]:.2f}")
    print(f"Chargeable Weight: {best[2]:.1f} kg")


# Main program
print("COURIER CHARGE OPTIMIZATION")

weight = float(input("Enter parcel weight (kg): "))
length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))

zone = input(
    "Enter distance zone (local/regional/national): "
).lower()

urgency = input(
    "Enter urgency (standard/express/same-day): "
).lower()

restricted = input(
    "Does the parcel need special handling? (yes/no): "
).lower() == "yes"

if weight <= 0 or min(length, width, height) <= 0:
    print("Invalid parcel dimensions or weight.")
else:
    optimize_courier(
        weight, length, width, height,
        zone, urgency, restricted
    )
