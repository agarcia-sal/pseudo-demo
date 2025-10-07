def check_dict_case(dict) -> bool:
    keys_list = list(dict.keys())
    if len(keys_list) == 0:
        return False
    state = "start"
    index = 0
    keys_length = len(keys_list)
    while index < keys_length:
        key = keys_list[index]
        if not isinstance(key, str):
            state = "mixed"
            break
        if state == "start":
            if key.isupper():
                state = "upper"
            elif key.islower():
                state = "lower"
            else:
                break
        elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
            state = "mixed"
            break
        else:
            break
        index += 1
    return state == "upper" or state == "lower"