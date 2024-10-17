student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# .items() returns a tuple, like (Rolf, 96), so we can use
# student, attendance.
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")