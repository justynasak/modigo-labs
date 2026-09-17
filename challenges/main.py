def count_items(items):
    # TODO: use a for loop to build a dictionary counting each item in `items`
    dick = {}
    for item in items:
        dick[item] = dick.get(item,0) + 1
    return dick