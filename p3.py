
# Hospital Billing and Patient Classification

def calculate_bill(consultation, diagnostic, treatment, patient_type):
    subtotal = consultation + diagnostic + treatment

    # Conditional concessions
    if patient_type == "Senior Citizen":
        concession_rate = 15
    elif patient_type == "Student":
        concession_rate = 10
    elif patient_type == "Staff":
        concession_rate = 20
    else:
        concession_rate = 0

    concession = subtotal * concession_rate / 100
    final_bill = subtotal - concession

    return subtotal, concession, final_bill


def classify_patient(final_bill, payment):
    if payment >= final_bill:
        return "Fully Paid"
    elif payment > 0:
        return "Partially Paid"
    else:
        return "Payment Pending"


def main():
    print("HOSPITAL BILLING SYSTEM")
    print("-----------------------")

    patient_name = input("Enter patient name: ")
    patient_type = input(
        "Enter patient type (General/Senior Citizen/Student/Staff): "
    ).strip().title()

    consultation = float(input("Enter consultation charge: Rs. "))
    diagnostic = float(input("Enter diagnostic charge: Rs. "))
    treatment = float(input("Enter treatment charge: Rs. "))

    if not patient_name.strip():
        print("Error: Patient name cannot be empty.")
        return

    if patient_type not in [
        "General", "Senior Citizen", "Student", "Staff"
    ]:
        print("Error: Invalid patient type.")
        return

    if min(consultation, diagnostic, treatment) < 0:
        print("Error: Charges cannot be negative.")
        return

    subtotal, concession, final_bill = calculate_bill(
        consultation, diagnostic, treatment, patient_type
    )

    print("\nBILL SUMMARY")
    print("-----------------------")
    print("Patient Name:", patient_name)
    print("Patient Type:", patient_type)
    print(f"Consultation Charge: Rs. {consultation:.2f}")
    print(f"Diagnostic Charge:  Rs. {diagnostic:.2f}")
    print(f"Treatment Charge:   Rs. {treatment:.2f}")
    print(f"Subtotal:           Rs. {subtotal:.2f}")
    print(f"Concession:         Rs. {concession:.2f}")
    print(f"Final Bill:         Rs. {final_bill:.2f}")

    payment = float(input("\nEnter amount paid: Rs. "))

    if payment < 0:
        print("Error: Payment cannot be negative.")
        return

    if payment > final_bill:
        refund = payment - final_bill
        balance = 0
    else:
        refund = 0
        balance = final_bill - payment

    status = classify_patient(final_bill, payment)

    print("\nPAYMENT DETAILS")
    print("-----------------------")
    print(f"Amount Paid: Rs. {payment:.2f}")
    print(f"Balance Due: Rs. {balance:.2f}")
    print(f"Refund:      Rs. {refund:.2f}")
    print("Payment Classification:", status)


if __name__ == "__main__":
    main()
