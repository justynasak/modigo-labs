def multiplication_table(number, limit):
    # TODO: use a for loop to build a list of number * 1 through number * limit
    answer = []
    if not limit:
        return []
    for n in range(1,limit+1):
        answer.append(n*number)
    return answer