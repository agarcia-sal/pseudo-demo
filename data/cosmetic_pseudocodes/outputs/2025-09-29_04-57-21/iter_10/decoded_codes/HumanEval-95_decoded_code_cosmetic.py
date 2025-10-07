from typing import Any, Dict

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    mode: str = "start"
    key_list = list(dictionary.keys())
    index: int = 0

    while index < len(key_list):
        current_key = key_list[index]

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
        elif (mode == "upper" and current_key != current_key.upper()) or (mode == "lower" and current_key != current_key.lower()):
            mode = "mixed"
            break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"