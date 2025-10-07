def check_dict_keys_case(d):
    if not d:
        return False
    state = "start"
    for key in d.keys():
        if not isinstance(key, str):
            state = "mixed"
            break
        if state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                state = "mixed"
                break
        elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
            state = "mixed"
            break
    return state == "upper" or state == "lower"