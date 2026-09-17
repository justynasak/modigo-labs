def items_to_restock(current_stock, minimum_levels):
    # TODO: loop through current_stock, compare against minimum_levels,
    # and return a list of item names below their minimum
    restock = []
    for item,quantity in current_stock.items():
        if item not in minimum_levels:
            continue
        if quantity < minimum_levels[item]:
            restock.append(item)
    return restock