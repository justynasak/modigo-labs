def total_word_count(sentences):
    count = 0
    for sentence in sentences:
        count += len(sentence.split())
    return count