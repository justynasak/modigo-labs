def run_with_retries(results, max_attempts=3, on_failure="skip", log=None):
    # TODO: handle the mutable default argument problem correctly —
    # do not use a mutable object like [] directly as a default value.
    # Then simulate retrying through `results` according to the rules described.
    if log is None:
        log = []
    attempts = 0
    for key in results:
        if attempts >= max_attempts:
            break
        attempts +=1

        if key == "success":
            log.append("success")
            break
        elif key == "fail" and on_failure == "log":
            log.append("attempt failed")
    return log