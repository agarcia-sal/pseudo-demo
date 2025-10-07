from typing import Any, Dict


def check_dict_case(input_map: Dict[Any, Any]) -> bool:
    keys_list = list(input_map.keys())
    if not keys_list:
        return False
    current_mode = "start"
    idx = 0
    while idx < len(keys_list):
        element = keys_list[idx]
        if not isinstance(element, str):
            current_mode = "mixed"
            break
        if current_mode == "start":
            if element.isupper():
                current_mode = "upper"
            else:
                if element.islower():
                    current_mode = "lower"
                else:
                    break
        elif current_mode == "upper":
            if not element.isupper():
                current_mode = "mixed"
                break
        elif current_mode == "lower":
            if not element.islower():
                current_mode = "mixed"
                break
        if current_mode == "mixed":
            break
        idx += 1
    return current_mode == "upper" or current_mode == "lower"