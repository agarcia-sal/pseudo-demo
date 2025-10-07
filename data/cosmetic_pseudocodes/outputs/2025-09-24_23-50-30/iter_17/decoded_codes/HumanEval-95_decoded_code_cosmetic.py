from typing import Mapping, Any

def check_dict_case(input_map: Mapping[Any, Any]) -> bool:
    if len(input_map) == 0:
        return False
    mode: str = "start"
    idx: int = 0
    keys_array = list(input_map.keys())
    while idx < len(keys_array):
        current_key = keys_array[idx]
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
        idx += 1
    return mode == "upper" or mode == "lower"