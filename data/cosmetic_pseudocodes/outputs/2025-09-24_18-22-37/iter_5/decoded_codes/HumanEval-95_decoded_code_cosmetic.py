from typing import Any, Dict

def check_dict_case(map_input: Dict[Any, Any]) -> bool:
    if not map_input:
        return False

    mode: str = "start"
    idx: int = 0
    keys_list = list(map_input.keys())

    while idx < len(keys_list):
        current_key = keys_list[idx]

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
        else:
            if mode == "upper":
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