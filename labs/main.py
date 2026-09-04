def get_student_grade(students, name):
    lookup = {}
    # TODO: loop through `students` and populate `lookup` with name -> grade

    # TODO: return the grade for `name` from `lookup`, or "Not found" if missing
    for student in students:
        lookup[student["name"]] = student["grade"]

    return lookup.get(name,"Not found")