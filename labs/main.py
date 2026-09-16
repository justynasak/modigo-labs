def find_index(numbers, target):
    # TODO: locate `target` in the sorted list `numbers` and return its index,
    # or -1 if it isn't there
    if not numbers:
        return -1

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1