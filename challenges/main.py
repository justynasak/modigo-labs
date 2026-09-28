def filter_and_group(catalog, required_tags, excluded_tags):
    # TODO: filter `catalog` by required_tags (must have all) and excluded_tags
    # (must have none), then group matching product names by category
    result = {}
    for product in catalog:
        tags = product["tags"]
        if required_tags <= tags and not (excluded_tags & tags):
            result.setdefault(product["category"],[]).append(product["name"])
    return result