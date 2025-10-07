def check_dict_case(dict) -> bool:
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        keys_list = []
        key_index = 0
        keys_list = []
        for key_element in dict:
            keys_list.append(key_element)
        key_index = 0
        while key_index < len(keys_list):
            key = keys_list[key_index]
            if type(key) != str:
                state = "mixed"
                break
            if state == "start":
                if key.isupper() == True:
                    state = "upper"
                elif key.islower() == True:
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
            else:
                break
            key_index += 1
        return (state == "upper") or (state == "lower")