
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 0.05
REBATE_RATE = 0.10
INCREASE_LIMIT = 30  # Percentage increase warning limit


def calculate_energy_charge(units):
    charge = 0

    # Slab 1: First 100 units
    slab1 = min(units, 100)
    charge += slab1 * 2.00

    # Slab 2: 101 to 200 units
    slab2 = min(max(units - 100, 0), 100)
    charge += slab2 * 3.00

    # Slab 3: 201 to 300 units
    slab3 = min(max(units - 200, 0), 100)
    charge += slab3 * 5.00

    # Slab 4: Above 300 units
    slab4 = max(units - 300, 0)
    charge += slab4 * 7.00

    return charge


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    surcharge = energy_charge * SURCHARGE_RATE
    subtotal = energy_charge + FIXED_CHARGE + surcharge

    # Give 10% rebate when consumption is 100 units or less
    rebate = subtotal * REBATE_RATE if units <= 100 else 0

    total_bill = subtotal - rebate

    return energy_charge, surcharge, rebate, total_bill


def main():
    months = []
    print("PROGRESSIVE ELECTRICITY BILLING SYSTEM")

    n = int(input("Enter number of months: "))

    for i in range(n):
        month = input(f"\nEnter month {i + 1}: ")
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Units cannot be negative. Try again.")
            return

        energy, surcharge, rebate, total = calculate_bill(units)

        months.append({
            "month": month,
            "units": units,
            "energy": energy,
            "surcharge": surcharge,
            "rebate": rebate,
            "total": total
        })

    print("\nMONTHLY ELECTRICITY BILL REPORT")
    print("-" * 85)
    print(f"{'Month':<12}{'Units':>8}{'Energy':>12}"
          f"{'Surcharge':>12}{'Rebate':>12}{'Total':>14}")
    print("-" * 85)

    for bill in months:
        print(f"{bill['month']:<12}{bill['units']:>8.1f}"
              f"{bill['energy']:>12.2f}"
              f"{bill['surcharge']:>12.2f}"
              f"{bill['rebate']:>12.2f}"
              f"{bill['total']:>14.2f}")

    print("\nMONTH-TO-MONTH COMPARISON")
    for i in range(1, len(months)):
        previous = months[i - 1]["total"]
        current = months[i]["total"]
        difference = current - previous

        if previous > 0:
            increase = (difference / previous) * 100
        else:
            increase = 0

        print(f"{months[i]['month']}: "
              f"Change = Rs. {difference:.2f} "
              f"({increase:.2f}%)")

        if increase > INCREASE_LIMIT:
            print("  WARNING: Unusual increase detected!")
        elif increase < 0:
            print("  Bill decreased compared to previous month.")

    if months:
        highest = max(months, key=lambda x: x["total"])
        lowest = min(months, key=lambda x: x["total"])

        print("\nHIGHEST BILL:", highest["month"],
              "- Rs.", round(highest["total"], 2))
        print("LOWEST BILL:", lowest["month"],
              "- Rs.", round(lowest["total"], 2))


if __name__ == "__main__":
    main()
