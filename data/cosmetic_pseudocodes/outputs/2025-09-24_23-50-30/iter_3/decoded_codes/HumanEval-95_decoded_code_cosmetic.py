from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys_list = list(dictionary.keys())
    if not keys_list:
        return False

    current_state = "start"
    index = 0
    while index < len(keys_list):
        current_key = keys_list[index]
        if not isinstance(current_key, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if current_key == current_key.upper():
                current_state = "upper"
            elif current_key == current_key.lower():
                current_state = "lower"
            else:
                break
        elif (current_state == "upper" and current_key != current_key.upper()) or (
            current_state == "lower" and current_key != current_key.lower()
        ):
            current_state = "mixed"
            break
        else:
            break
        index += 1

    return current_state == "upper" or current_state == "lower"