def build_countdown(start):
    countdown = []
    # TODO: use a for loop with range() to count down from `start` to 1,
    # appending each number to `countdown`
    if not start:
        return []
    for n in range(start,0,-1):
        countdown.append(n)
    return countdown