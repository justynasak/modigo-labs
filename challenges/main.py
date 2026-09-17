def has_conflict(meetings):
    # TODO: return True if any two meetings overlap in time, False otherwise
    if not meetings or len(meetings) < 2:
        return False
    
    sorted_meetings = sorted(meetings,key = lambda x : x[0])
    for i in range(len(sorted_meetings)-1):
        current_end = sorted_meetings[i][1]
        next_start = sorted_meetings[i + 1][0]
        if next_start < current_end:
            return True
        else:
            return False
    return False