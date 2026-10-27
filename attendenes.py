
# Attendance Recovery Computation

import math


def calculate_attendance(attended, conducted):
    if conducted == 0:
        return 0
    return (attended / conducted) * 100


def minimum_classes_needed(attended, conducted, threshold):
    if conducted == 0:
        return 0

    if attended / conducted * 100 >= threshold:
        return 0

    # Solve: (attended + x) / (conducted + x) >= threshold / 100
    required = (
        threshold * conducted - 100 * attended
    ) / (100 - threshold)

    return max(0, math.ceil(required))


def main():
    print("ATTENDANCE RECOVERY COMPUTATION")
    print("--------------------------------")

    attended = int(input("Enter classes attended: "))
    conducted = int(input("Enter total classes conducted: "))
    threshold = float(input("Enter eligibility percentage: "))

    if conducted < 0 or attended < 0 or attended > conducted:
        print("Invalid attendance details.")
        return

    if not 0 < threshold <= 100:
        print("Threshold must be greater than 0 and at most 100.")
        return

    current = calculate_attendance(attended, conducted)

    print(f"\nCurrent Attendance: {current:.2f}%")
    print(f"Required Attendance: {threshold:.2f}%")

    if current >= threshold:
        print("Status: Eligible")
        print("Additional classes required: 0")
    elif threshold == 100:
        print("A 100% attendance target cannot be reached")
        print("by attending more classes after any absence.")
        return
    else:
        needed = minimum_classes_needed(
            attended, conducted, threshold
        )

        print("Status: Not eligible")
        print("Minimum consecutive classes to attend:", needed)

    print("\nFUTURE ATTENDANCE SCENARIOS")
    print("--------------------------------")

    scenarios = [5, 10, 15, 20]

    for future_classes in scenarios:
        # Assume the student attends every future class
        future_attended = attended + future_classes
        future_total = conducted + future_classes

        future_percentage = calculate_attendance(
            future_attended, future_total
        )

        print(
            f"After attending {future_classes} classes: "
            f"{future_percentage:.2f}%"
        )

        if future_percentage >= threshold:
            print("  Eligibility achieved.")
        else:
            extra = minimum_classes_needed(
                future_attended, future_total, threshold
            )
            print(f"  More classes needed: {extra}")


if __name__ == "__main__":
    main()
