def longest_streaks(daily_records):
    # TODO: identify all students across every day, then track each student's
    # current and longest streak of consecutive "present" days
    if not daily_records:
        return {}
    students = set()
    for day in daily_records:
        students.update(day.keys())
    
    longest = {student : 0 for student in students}
    current = {student : 0 for student in students}

    for day in daily_records:
        for student in students:
            status = day.get(student,"absent")
            if status == "present":
                current[student] += 1
                if current[student] > longest[student]:
                    longest[student] = current[student]
            else:
                current[student] = 0
    
    return longest