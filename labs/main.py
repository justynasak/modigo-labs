def unmatched_skus(warehouse_a, warehouse_b):
    # TODO: compute the symmetric difference using union/intersection/difference,
    # without using ^ or .symmetric_difference()
    return set(warehouse_a) - set(warehouse_b) | set(warehouse_b) - set(warehouse_a)