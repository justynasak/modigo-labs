def sum_of_digits(number):
    # TODO: use a for loop to add up each digit of `number`
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum