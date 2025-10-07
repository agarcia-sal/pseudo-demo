from typing import Any, Dict


def check_dict_case(recan_var: Dict[Any, Any]) -> bool:
    if len(recan_var) == 0:
        return False

    bruv_stat: str = "start"
    grol_loop = list(recan_var.keys())
    idx_pos = 0

    while idx_pos < len(grol_loop):
        zink_val = grol_loop[idx_pos]

        if not isinstance(zink_val, str):
            bruv_stat = "mixed"
            break

        if bruv_stat == "start":
            if zink_val.isupper():
                bruv_stat = "upper"
            elif zink_val.islower():
                bruv_stat = "lower"
            else:
                break
        elif bruv_stat == "upper":
            if not zink_val.isupper():
                bruv_stat = "mixed"
                break
        elif bruv_stat == "lower":
            if not zink_val.islower():
                bruv_stat = "mixed"
                break
        else:
            break

        idx_pos += 1

    return bruv_stat == "upper" or bruv_stat == "lower"