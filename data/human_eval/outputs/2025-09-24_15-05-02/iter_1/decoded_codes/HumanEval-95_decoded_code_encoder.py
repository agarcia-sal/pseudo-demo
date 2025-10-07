def check_dict_keys_case(d):
    if d == {}:
        return False
    state = "start"
    for k in d.keys():
        if not isinstance(k, str):
            state = "mixed"
            break
        if state == "start":
            if k.isupper():
                state = "upper"
            elif k.islower():
                state = "lower"
            else:
                break
        elif (state == "upper" and not k.isupper()) or (state == "lower" and not k.islower()):
            state = "mixed"
            break
    return state == "upper" or state == "lower"