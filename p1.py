Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = [
    {
        "name": "Ravi",
        "marks": [85, 90, 80, 88],
        "attendance": 90,
        "income": 180000
    },
    {
        "name": "Priya",
        "marks": [92, 88, 90, 95],
        "attendance": 95,
        "income": 200000
    },
    {
        "name": "Kiran",
        "marks": [70, 80, 75, 85],
        "attendance": 80,
        "income": 150000
    },
    {
        "name": "Anu",
        "marks": [85, 90, 80, 88],
        "attendance": 92,
        "income": 120000
    },
    {
        "name": "Suresh",
        "marks": [80, 75, 82, 78],
        "attendance": 70,
        "income": 100000
    }
]

eligible_students = []
rejected_students = []

# Evaluate eligibility
for student in students:
    aggregate = sum(student["marks"]) / len(student["marks"])

    if (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARKS
                for mark in student["marks"])
        and student["attendance"] >= MIN_ATTENDANCE
        and student["income"] <= MAX_INCOME
    ):
        student["aggregate"] = aggregate
        eligible_students.append(student)
    else:
        rejected_students.append(student["name"])

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"]
    )
)

# Display results
print("\n===== UNIVERSITY SCHOLARSHIP RESULTS =====")

print("\nEligible Students - Ranked List:")
if eligible_students:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"{rank}. {student['name']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs.{student['income']}"
        )
else:
    print("No eligible students found.")

print("\nRejected Students:")
if rejected_students:
    for name in rejected_students:
        print(name)
else:
    print("None")

