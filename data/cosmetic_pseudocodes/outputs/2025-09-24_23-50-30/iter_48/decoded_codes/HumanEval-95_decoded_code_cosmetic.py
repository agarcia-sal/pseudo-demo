from typing import Any, Dict


def check_dict_case(dict_param: Dict[Any, Any]) -> bool:
    if not dict_param:
        return False
    mode_var: str = "start"
    key_iter = list(dict_param.keys())
    idx_var = 0
    while idx_var < len(key_iter):
        cur_key = key_iter[idx_var]
        idx_var += 1
        if not isinstance(cur_key, str):
            mode_var = "mixed"
            break
        if mode_var == "start":
            if cur_key.upper() == cur_key:
                mode_var = "upper"
            elif cur_key.lower() == cur_key:
                mode_var = "lower"
            else:
                break
        elif (mode_var == "upper" and cur_key.upper() != cur_key) or (
            mode_var == "lower" and cur_key.lower() != cur_key
        ):
            mode_var = "mixed"
            break
    return mode_var == "upper" or mode_var == "lower"