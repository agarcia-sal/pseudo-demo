from typing import Dict, Any

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    mode: str = "start"
    key_queue = list(dictionary.keys())

    while key_queue:
        current_key = key_queue.pop(0)

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key == current_key.upper():
                mode = "upper"
            else:
                if current_key != current_key.lower():
                    break
                mode = "lower"
        elif not ((mode == "upper" and current_key == current_key.upper()) or
                  (mode == "lower" and current_key == current_key.lower())):
            mode = "mixed"
            break
        else:
            break

    return mode == "upper" or mode == "lower"