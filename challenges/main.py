def build_roster(students):
    roster = {}
    # TODO: loop through `students` and group names by grade in `roster`
    if not students:
        return {}
    roster = {}
    for student,grade in students:
        roster.setdefault(grade,[]).append(student)
    return roster