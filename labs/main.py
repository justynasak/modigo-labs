def count_unique_visitors(visitors):
    # TODO: convert `visitors` to a set to remove duplicates, then return its length
    if not visitors:
        return 0
    number = len(set(visitors))
    return number