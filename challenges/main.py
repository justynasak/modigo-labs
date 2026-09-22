def rank_players(scores):
    # TODO: assign standard competition ranks based on score, handling ties correctly,
    # and return (name, rank) tuples in the original input order
    distict_sorted = sorted([score for _,score in scores],reverse = True)
    rank_map = {}
    for i,s in enumerate(distict_sorted):
        if s not in rank_map:
            rank_map[s] = i + 1
    return [(name,rank_map[score]) for name,score in scores]