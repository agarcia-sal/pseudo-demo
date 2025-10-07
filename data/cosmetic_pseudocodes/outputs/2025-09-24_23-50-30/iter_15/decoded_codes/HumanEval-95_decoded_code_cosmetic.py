from typing import Any


def check_dict_case(dictionary: dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    mode: str = "start"
    keys_list = list(dictionary.keys())
    index: int = 0

    while index < len(keys_list):
        current_key = keys_list[index]

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
        elif not ((mode == "upper" and current_key == current_key.upper()) or
                  (mode == "lower" and current_key == current_key.lower())):
            mode = "mixed"
            break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"