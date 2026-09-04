def analyze_survey(responses):
    tally = {}
    # TODO: loop through `responses` and populate `tally`
    for color in responses:
        tally[color] = tally.get(color,0) + 1
    if not tally:
        return {"tally": {}, "most_popular": None}

    most_popular = None
    highest_count = 0
    # TODO: loop through `tally` to find the color with the highest count
    # (keep the first one seen in case of a tie)
    for color,count in tally.items():
        if count > highest_count:
            highest_count = count
            most_popular = color
    
    return {"tally": tally, "most_popular": most_popular}