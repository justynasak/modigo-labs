def analyze_sales(prices):
    """
    Takes a list of prices and returns a summary dictionary
    with keys: total, average, highest, lowest.
    Do not use sum(), max(), or min() — use a for loop instead.
    """
    # Your code here
    adder = 0
    total = float(adder)
    high = prices[0]
    low = prices[0]
    for price in prices:
        total += float(price)
        if price > high:
            high = price
        if price < low:
            low = price

    ave = round(total/len(prices),2)
    return {
        "total" : total,
        "average" : ave,
        "highest" : high,
        "lowest" : low,
    }

print (analyze_sales([500,1200,300,4500,1200]))