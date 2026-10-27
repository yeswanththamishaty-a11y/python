
# Progressive Electricity Billing System

# Electricity slab rates (sample rates)
SLAB1_RATE = 2.00   # 0-100 units
SLAB2_RATE = 3.00   # 101-200 units
SLAB3_RATE = 5.00   # 201-300 units
SLAB4_RATE = 7.00   # Above 300 units

FIXED_CHARGE = 100
SURCHARGE_RATE = 5       # 5% surcharge
REBATE_RATE = 5          # 5% rebate if bill is below Rs. 1000
INCREASE_LIMIT = 30      # Flag increases above 30%

# Calculate progressive electricity charges
def calculate_energy_charge(units):
    if units <= 100:
        return units * SLAB1_RATE
    elif units <= 200:
        return (100 * SLAB1_RATE
                + (units - 100) * SLAB2_RATE)
    elif units <= 300:
        return (100 * SLAB1_RATE
                + 100 * SLAB2_RATE
                + (units - 200) * SLAB3_RATE)
    else:
        return (100 * SLAB1_RATE
                + 100 * SLAB2_RATE
                + 100 * SLAB3_RATE
                + (units - 300) * SLAB4_RATE)

# Calculate total bill
def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    subtotal = energy_charge + FIXED_CHARGE

    surcharge = subtotal * SURCHARGE_RATE / 100
    total_before_rebate = subtotal + surcharge

    rebate = 0
    if total_before_rebate < 1000:
        rebate = total_before_rebate * REBATE_RATE / 100

    total_bill = total_before_rebate - rebate

    return energy_charge, surcharge, rebate, total_bill

# Monthly consumption data
monthly_units = {
    "January": 120,
    "February": 140,
    "March": 160,
    "April": 230,
    "May": 350,
    "June": 280
}

monthly_bills = {}

print("===== PROGRESSIVE ELECTRICITY BILLING =====")

for month, units in monthly_units.items():
    energy, surcharge, rebate, total = calculate_bill(units)
    monthly_bills[month] = total

    print(f"\nMonth: {month}")
    print(f"Units Consumed: {units}")
    print(f"Energy Charge: Rs.{energy:.2f}")
    print(f"Fixed Charge: Rs.{FIXED_CHARGE:.2f}")
    print(f"Surcharge: Rs.{surcharge:.2f}")
    print(f"Rebate: Rs.{rebate:.2f}")
    print(f"Total Bill: Rs.{total:.2f}")

# Compare consecutive monthly bills
print("\n===== MONTHLY BILL COMPARISON =====")

months = list(monthly_bills.keys())

for i in range(1, len(months)):
    previous_month = months[i - 1]
    current_month = months[i]

    previous_bill = monthly_bills[previous_month]
    current_bill = monthly_bills[current_month]

    increase = current_bill - previous_bill
    percentage_change = (increase / previous_bill) * 100

    print(f"\n{previous_month} to {current_month}")
    print(f"Bill Change: Rs.{increase:.2f}")
    print(f"Percentage Change: {percentage_change:.2f}%")

    if percentage_change > INCREASE_LIMIT:
        print("Alert: Unusual bill increase detected!")
    elif percentage_change < 0:
        print("Bill decreased.")
    else:
        print("Bill change is within the expected limit.")

print("\n===== BILLING COMPLETED =====")
