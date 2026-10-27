
# Multi-Plan Telecommunications Cost Optimization

plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "data": 2,
        "calls": 100,
        "validity": 28,
        "extra_data": 20,
        "extra_call": 0.50
    },
    {
        "name": "Standard Plan",
        "price": 299,
        "data": 3,
        "calls": 200,
        "validity": 28,
        "extra_data": 15,
        "extra_call": 0.40
    },
    {
        "name": "Premium Plan",
        "price": 399,
        "data": 5,
        "calls": 300,
        "validity": 56,
        "extra_data": 10,
        "extra_call": 0.30
    },
    {
        "name": "Unlimited Plan",
        "price": 599,
        "data": 10,
        "calls": 500,
        "validity": 84,
        "extra_data": 5,
        "extra_call": 0.20
    }
]


def main():
    print("TELECOMMUNICATION COST OPTIMIZATION")
    print("-" * 40)

    data_used = float(input("Enter monthly data usage (GB): "))
    calls_used = int(input("Enter monthly call minutes: "))
    required_validity = int(input("Enter required validity (days): "))
    budget = float(input("Enter your budget (Rs.): "))

    if data_used < 0 or calls_used < 0:
        print("Usage cannot be negative.")
        return

    if required_validity <= 0 or budget < 0:
        print("Validity must be positive and budget non-negative.")
        return

    results = []

    for plan in plans:
        extra_data = max(0, data_used - plan["data"])
        extra_calls = max(0, calls_used - plan["calls"])

        data_charge = extra_data * plan["extra_data"]
        call_charge = extra_calls * plan["extra_call"]

        total_cost = plan["price"] + data_charge + call_charge

        eligible = (
            plan["validity"] >= required_validity
            and total_cost <= budget
        )

        results.append({
            "name": plan["name"],
            "price": plan["price"],
            "data_charge": data_charge,
            "call_charge": call_charge,
            "total": total_cost,
            "validity": plan["validity"],
            "eligible": eligible
        })

    print("\nPLAN COMPARISON")
    print("-" * 85)
    print(f"{'Plan':<17}{'Base':>8}{'Data Fee':>11}"
          f"{'Call Fee':>11}{'Total':>11}"
          f"{'Days':>7}{'Status':>12}")
    print("-" * 85)

    for r in results:
        status = "Eligible" if r["eligible"] else "Not eligible"
        print(f"{r['name']:<17}{r['price']:>8.2f}"
              f"{r['data_charge']:>11.2f}"
              f"{r['call_charge']:>11.2f}"
              f"{r['total']:>11.2f}"
              f"{r['validity']:>7}"
              f"{status:>12}")

    eligible_plans = [r for r in results if r["eligible"]]

    print("\nRECOMMENDATION")
    print("-" * 40)

    if eligible_plans:
        best = min(eligible_plans, key=lambda p: p["total"])

        print("Best Plan:", best["name"])
        print(f"Total Cost: Rs. {best['total']:.2f}")
        print("Validity:", best["validity"], "days")
        print(f"Budget Remaining: Rs. {budget - best['total']:.2f}")
    else:
        print("No plan satisfies all constraints.")
        print("Try increasing the budget or reducing requirements.")


if __name__ == "__main__":
    main()
