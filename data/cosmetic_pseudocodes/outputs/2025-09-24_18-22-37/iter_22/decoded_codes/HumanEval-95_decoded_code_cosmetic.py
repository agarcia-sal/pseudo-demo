from typing import Any, Mapping


def check_dict_case(map_var: Mapping[Any, Any]) -> bool:
    keys = list(map_var.keys())
    if not keys:
        return False
    mode: str = "start"
    iter_index: int = 0
    while iter_index < len(keys):
        current_item = keys[iter_index]
        iter_index += 1
        if not isinstance(current_item, str):
            mode = "mixed"
            break
        if mode == "start":
            if current_item == current_item.upper():
                mode = "upper"
            elif current_item == current_item.lower():
                mode = "lower"
            else:
                break
        else:
            if (mode == "upper" and current_item != current_item.upper()) or (mode == "lower" and current_item != current_item.lower()):
                mode = "mixed"
                break
            else:
                break
    result_flag = mode == "upper" or mode == "lower"
    return result_flag