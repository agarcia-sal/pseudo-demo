from typing import Dict, Any

def check_dict_case(d: Dict[Any, Any]) -> bool:
    if len(list(d.keys())) == 0:
        return False
    state = "start"
    keys_list = list(d.keys())
    index = 0
    while index < len(keys_list):
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