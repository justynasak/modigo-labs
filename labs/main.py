def top_words(text, n):
    # TODO: count word frequency (case-insensitive), then return the top `n`
    # as (word, count) tuples sorted by count descending, ties broken alphabetically
    if not text:
        return []
    words = text.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word,0)+1

    ranked = sorted(count.items(), key = lambda x: (-x[1],x[0]))

    return ranked[:n]