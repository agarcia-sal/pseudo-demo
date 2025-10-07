def check_dict_case(dict) -> bool:
    keys = list(dict.keys())
    length = len(keys)
    if length == 0:
        return False
    else:
        state = "start"
        index = 0
        length = len(keys)
        while index < length:
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
            else:
                if (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
                else:
                    break
            index += 1
        is_upper_state = (state == "upper")
        is_lower_state = (state == "lower")
        return is_upper_state or is_lower_state