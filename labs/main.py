def top_scorers(results):
    # TODO: find the highest score, collect all players who acheived it,
    # and return their names as a sorted tuple
   highest = max(score for _,score in results)
   winners = sorted(name for name, score in results if score == highest)
   return tuple(winners)