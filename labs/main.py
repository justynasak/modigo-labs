def word_lengths(words):
    lengths = {}
    # TODO: loop through `words` and populate `lengths` with word -> length of word
    for word in words:
        lengths[word] = len(word)
    return lengths