from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    current_state: str = "start"

    for key in dictionary.keys():
        if not isinstance(key, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if key == key.upper():
                current_state = "upper"
            elif key == key.lower():
                current_state = "lower"
            else:
                break
        elif current_state == "upper":
            if key != key.upper():
                current_state = "mixed"
                break
        elif current_state == "lower":
            if key != key.lower():
                current_state = "mixed"
                break

        if current_state == "mixed":
            break

    return current_state == "upper" or current_state == "lower"