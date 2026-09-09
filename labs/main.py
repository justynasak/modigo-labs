def count_unique_coordinates(coordinates):
    if not coordinates:
        return 0
    unique = set()
    for coord in coordinates:
        unique.add(coord)
    return len(unique)