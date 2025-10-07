from typing import Mapping, Any


def check_dict_case(arg_map: Mapping[Any, Any]) -> bool:
    if len(arg_map) <= 0:
        return False

    flag: str = "start"
    keys = list(arg_map.keys())
    idx = 0

    while idx < len(keys):
        key_val = keys[idx]
        if not isinstance(key_val, str):
            flag = "mixed"
            break

        if flag == "start":
            if key_val == key_val.upper():
                flag = "upper"
            elif key_val == key_val.lower():
                flag = "lower"
            else:
                break
        else:
            cond1 = flag == "upper" and key_val != key_val.upper()
            cond2 = flag == "lower" and key_val != key_val.lower()
            if cond1 or cond2:
                flag = "mixed"
            break

        idx += 1

    return flag == "upper" or flag == "lower"