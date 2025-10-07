from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    current_state = "start"

    for key in dictionary.keys():
        if not isinstance(key, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if key.isupper():
                current_state = "upper"
            elif key.islower():
                current_state = "lower"
            else:
                break
        elif (current_state == "upper" and not key.isupper()) or (current_state == "lower" and not key.islower()):
            current_state = "mixed"
            break
        else:
            break

    return current_state == "upper" or current_state == "lower"