from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    keys_list = list(dictionary.keys())
    if len(keys_list) <= 0:
        return False

    current_state = "start"

    for element in keys_list:
        if not isinstance(element, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if element == element.upper():
                current_state = "upper"
            elif element == element.lower():
                current_state = "lower"
            else:
                break
        else:
            if (current_state == "upper" and element != element.upper()) or (
                current_state == "lower" and element != element.lower()
            ):
                current_state = "mixed"
                break
            else:
                break

    return current_state == "upper" or current_state == "lower"