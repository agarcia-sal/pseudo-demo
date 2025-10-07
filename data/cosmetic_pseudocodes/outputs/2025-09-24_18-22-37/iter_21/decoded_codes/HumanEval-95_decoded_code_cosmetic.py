from typing import Mapping, Any

def check_dict_case(assoc_array: Mapping[Any, Any]) -> bool:
    keys = list(assoc_array.keys())
    if not keys:
        return False

    mode: str = "start"

    for current_key in keys:
        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            elif current_key == current_key.lower():
                mode = "lower"
            else:
                break
        elif mode == "upper":
            if current_key != current_key.upper():
                mode = "mixed"
                break
        elif mode == "lower":
            if current_key != current_key.lower():
                mode = "mixed"
                break
        else:
            break

    return mode == "upper" or mode == "lower"