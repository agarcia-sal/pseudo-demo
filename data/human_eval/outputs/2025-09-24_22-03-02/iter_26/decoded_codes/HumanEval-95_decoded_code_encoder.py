def check_dict_case(dict) -> bool:
    keys_list = list(dict.keys())
    if len(keys_list) == 0:
        return False
    else:
        state = "start"
        for key in keys_list:
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
            elif state == "upper":
                if not key.isupper():
                    state = "mixed"
                    break
            elif state == "lower":
                if not key.islower():
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower"