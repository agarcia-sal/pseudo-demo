def check_dict_case(dict) -> bool:
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        keys = list(dict.keys())
        index = 0
        while index < len(keys):
            key = keys[index]
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
            elif state == "upper" and not key.isupper():
                state = "mixed"
                break
            elif state == "lower" and not key.islower():
                state = "mixed"
                break
            else:
                break
            index += 1
        return state == "upper" or state == "lower"