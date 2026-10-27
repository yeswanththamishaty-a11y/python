
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
    print("----------------------------------")

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
        # Calculate excess usage charges
        extra_data_used = max(0, data_used - plan["data"])
        extra_calls_used = max(0, calls_used - plan["calls"])

        data_charge = extra_data_used * plan["extra_data"]
        call_charge = extra_calls_used * plan["extra_call"]

        total_cost = plan["price"] + data_charge + call_charge

        # Check plan constraints
        eligible = (
            plan["validity"] >= required_validity
            and total_cost <= budget
        )

        results.append({
            "name": plan["name"],
            "base_price": plan["price"],
            "data_charge": data_charge,
            "call_charge": call_charge,
            "total_cost": total_cost,
            "validity": plan["validity"],
            "eligible": eligible
        })

    print("\nPLAN COMPARISON")
    print("-" * 90)
    print(f"{'Plan':<18}{'Base':>9}{'Data Fee':>12}"
          f"{'Call Fee':>12}{'Total':>12}"
          f"{'Days':>8}{'Status':>12}")
    print("-" * 90)

    for result in results:
        status = "Eligible" if result["eligible"] else "Not eligible"

        print(f"{result['name']:<18}"
              f"{result['base_price']:>9.2f}"
              f"{result['data_charge']:>12.2f}"
              f"{result['call_charge']:>12.2f}"
              f"{result['total_cost']:>12.2f}"
              f"{result['validity']:>8}"
              f"{status:>12}")

    eligible_plans = [
        result for result in results if result["eligible"]
    ]

    print("\nRECOMMENDATION")

    if eligible_plans:
        best_plan = min(
            eligible_plans,
            key=lambda plan: plan["total_cost"]
        )

        print("Most economical plan:", best_plan["name"])
        print("Total estimated cost: Rs.",
              round(best_plan["total_cost"], 2))
        print("Validity:", best_plan["validity"], "days")
        print("Budget remaining: Rs.",
              round(budget - best_plan["total_cost"], 2))
    else:
        print("No plan satisfies all your requirements.")
        print("Consider increasing your budget or reducing usage.")


if __name__ == "__main__":
    main()
