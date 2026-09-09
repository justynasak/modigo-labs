def dedupe_preserve_order(items):
    # TODO: use a set to track seen values while building a new list
    # that preserves the original order of first appearances
    if not items:
        return []
    dedupe = set()
    result = []
    for item in items:
        if item not in dedupe:
            dedupe.add(item)
            result.append(item)
    return result