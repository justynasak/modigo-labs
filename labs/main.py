def group_by_grade(students):
    # TODO: determine each student's letter grade and group their names by grade band
    grades = {}
    for student in students:
        score = student["score"]

        if score >= 90:
            band = "A"
        elif score >= 80:
            band = "B"
        elif score >= 70:
            band = "C"
        elif score >= 60:
            band = "D"
        else:
            band = "F"
        grades.setdefault(band,[]).append(student["name"])
    return grades