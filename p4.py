
# Employee Payroll and Deduction Analysis

def calculate_tax(taxable_salary):
    # Illustrative progressive monthly deduction slabs
    if taxable_salary <= 20000:
        tax = 0
    elif taxable_salary <= 40000:
        tax = (taxable_salary - 20000) * 0.05
    elif taxable_salary <= 60000:
        tax = 1000 + (taxable_salary - 40000) * 0.10
    else:
        tax = 3000 + (taxable_salary - 60000) * 0.15

    return tax


def main():
    print("EMPLOYEE PAYROLL SYSTEM")
    print("=" * 40)

    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")

    basic = float(input("Enter basic salary (Rs.): "))
    hra = float(input("Enter house rent allowance (Rs.): "))
    da = float(input("Enter dearness allowance (Rs.): "))
    other_allowances = float(input("Enter other allowances (Rs.): "))

    overtime_hours = float(input("Enter overtime hours: "))
    overtime_rate = float(input("Enter overtime rate per hour (Rs.): "))
    incentives = float(input("Enter incentives (Rs.): "))

    # Validate inputs
    amounts = [
        basic, hra, da, other_allowances,
        overtime_hours, overtime_rate, incentives
    ]

    if not employee_id.strip() or not name.strip():
        print("Error: Employee ID and name are required.")
        return

    if any(value < 0 for value in amounts):
        print("Error: Salary values cannot be negative.")
        return

    overtime_pay = overtime_hours * overtime_rate

    gross_salary = (
        basic + hra + da + other_allowances
        + overtime_pay + incentives
    )

    # Illustrative deductions
    provident_fund = basic * 0.12
    professional_tax = 200 if gross_salary > 15000 else 0
    income_tax = calculate_tax(gross_salary)

    total_deductions = (
        provident_fund + professional_tax + income_tax
    )

    net_salary = gross_salary - total_deductions

    # Salary statement
    print("\n" + "=" * 48)
    print("             SALARY STATEMENT")
    print("=" * 48)
    print(f"Employee ID       : {employee_id}")
    print(f"Employee Name     : {name}")
    print("-" * 48)

    print("EARNINGS")
    print(f"Basic Salary      : Rs. {basic:10.2f}")
    print(f"HRA               : Rs. {hra:10.2f}")
    print(f"Dearness Allowance: Rs. {da:10.2f}")
    print(f"Other Allowances  : Rs. {other_allowances:10.2f}")
    print(f"Overtime Pay      : Rs. {overtime_pay:10.2f}")
    print(f"Incentives        : Rs. {incentives:10.2f}")
    print("-" * 48)
    print(f"Gross Salary      : Rs. {gross_salary:10.2f}")

    print("\nDEDUCTIONS")
    print(f"Provident Fund    : Rs. {provident_fund:10.2f}")
    print(f"Professional Tax  : Rs. {professional_tax:10.2f}")
    print(f"Income Tax        : Rs. {income_tax:10.2f}")
    print("-" * 48)
    print(f"Total Deductions  : Rs. {total_deductions:10.2f}")
    print(f"NET SALARY        : Rs. {net_salary:10.2f}")
    print("=" * 48)


if __name__ == "__main__":
    main()
