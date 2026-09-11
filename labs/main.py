def resolve_settings(base_config=None, override=None, built_in_defaults=None):
    # TODO: handle the mutable default argument problem for all three dict parameters.
    # Then resolve each of the four known settings by checking override first,
    # then base_config, then built_in_defaults — using "key exists" checks,
    # NOT truthiness checks, since 0/False/"" are valid explicit values.
    if base_config is None:
        base_config = {}
    if override is None:
        override = {}
    if built_in_defaults is None:
        built_in_defaults = {"timeout":30,"retries":3,"verbose":False,"cache":True}
    resolved = {}
    for key in ("timeout","retries","verbose","cache"):
        if key in override:
            resolved[key] = override[key]
        elif key in base_config:
            resolved[key] = base_config[key]
        else:
            resolved[key] = built_in_defaults[key]
    
    return resolved