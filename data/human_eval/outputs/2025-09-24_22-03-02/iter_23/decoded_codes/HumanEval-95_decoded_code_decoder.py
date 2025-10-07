def check_dict_case(dict) -> bool:
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        keys_list = list(dict.keys())
        keys_count = len(keys_list)
        index = 0
        while index < keys_count:
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