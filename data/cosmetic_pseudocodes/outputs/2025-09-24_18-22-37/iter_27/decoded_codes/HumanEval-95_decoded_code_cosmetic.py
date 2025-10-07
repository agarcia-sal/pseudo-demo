from typing import Dict, Any


def check_dict_case(flag_map: Dict[Any, Any]) -> bool:
    keys = list(flag_map.keys())
    if len(keys) == 0:
        return False

    h_flag: str = "start"
    idx: int = 0

    while idx < len(keys):
        k = keys[idx]

        if not isinstance(k, str):
            h_flag = "mixed"
            break

        if h_flag == "start":
            if k == k.upper():
                h_flag = "upper"
            elif k == k.lower():
                h_flag = "lower"
            else:
                break
        else:
            if (h_flag == "upper" and k != k.upper()) or (h_flag == "lower" and k != k.lower()):
                h_flag = "mixed"
                break
            else:
                break
        idx += 1

    return h_flag == "upper" or h_flag == "lower"