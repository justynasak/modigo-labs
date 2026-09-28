def all_unique_tags(posts):
    if not posts:
        return set()
    tags = set()
    for post in posts:
        tags.update(post["tags"])
    return tags