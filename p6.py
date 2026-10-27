
# Student Timetable Conflict Detection

# Course schedules: (course, day, start_time, end_time, room)
courses = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Web Development", "Monday", "09:30", "10:30", "R102"),
    ("Computer Networks", "Monday", "10:00", "11:00", "R101"),
    ("Mathematics", "Tuesday", "09:00", "10:00", "R103")
]

# Rooms that are unavailable at specific times
unavailable_rooms = [
    ("R101", "Monday", "10:00", "11:00")
]

# Convert HH:MM time into minutes
def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

# Check whether two time periods overlap
def overlaps(start1, end1, start2, end2):
    return (
        to_minutes(start1) < to_minutes(end2)
        and to_minutes(start2) < to_minutes(end1)
    )

def validate_timetable(schedule):
    conflicts = []

    for i in range(len(schedule)):
        course1 = schedule[i]
        name1, day1, start1, end1, room1 = course1

        # Check unavailable rooms
        for room, day, start, end in unavailable_rooms:
            if (
                room1 == room
                and day1 == day
                and overlaps(start1, end1, start, end)
            ):
                conflicts.append(
                    f"{name1}: Room {room1} is unavailable "
                    f"on {day1} ({start1}-{end1})."
                )

        # Compare each course with the remaining courses
        for j in range(i + 1, len(schedule)):
            course2 = schedule[j]
            name2, day2, start2, end2, room2 = course2

            if day1 == day2 and overlaps(
                start1, end1, start2, end2
            ):
                # Same student cannot attend two classes at once
                conflicts.append(
                    f"Time conflict: {name1} and {name2} "
                    f"overlap on {day1}."
                )

                # Two classes cannot use the same room simultaneously
                if room1 == room2:
                    conflicts.append(
                        f"Room conflict: {room1} is booked by "
                        f"{name1} and {name2} simultaneously."
                    )

    return conflicts


# Validate the proposed timetable
print("STUDENT TIMETABLE VALIDATION")
print("-" * 35)

conflicts = validate_timetable(courses)

if conflicts:
    for conflict in conflicts:
        print("CONFLICT:", conflict)
else:
    print("Timetable is valid. No conflicts found.")
