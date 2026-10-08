def build_roster(students):
    roster = {}
    # TODO: loop through `students` and group names by grade in `roster`
    for name,grade in students:
        roster.setdefault(grade,[]).append(name)
    return roster

print(build_roster([("Ada",5),("Bola",6),("Chide",5)]))