def path_hits_blocked(blocked, path):
    # TODO: check whether any position in `path` also appears in `blocked`
    if not path:
        return False
    for pos in path:
        if pos in blocked:
            return True
    return False