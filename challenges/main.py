def smart_title_case(sentence):
    # TODO: capitalize each word except connector words (a, an, the, of, in, on, and),
    # unless that connector word is the first word in the sentence
    connectors = {"a","an","the","of","in","on","and"}
    words = sentence.split(" ")
    result = []
    for i,word in enumerate(words):
        if i != 0 and word in connectors:
            result.append(word)
        else:
            result.append(word[0].upper()+word[1:])
    return " ".join(result)