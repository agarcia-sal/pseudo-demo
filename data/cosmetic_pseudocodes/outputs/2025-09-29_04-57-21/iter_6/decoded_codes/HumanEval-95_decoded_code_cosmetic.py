from typing import Any, Dict

def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    mode: str = "start"
    for key_element in dictionary.keys():
        if not isinstance(key_element, str):
            mode = "mixed"
            break

        if mode == "start":
            if key_element == key_element.upper():
                mode = "upper"
            elif key_element == key_element.lower():
                mode = "lower"
            else:
                break
        else:
            if (mode == "upper" and key_element != key_element.upper()) or \
               (mode == "lower" and key_element != key_element.lower()):
                mode = "mixed"
                break
            else:
                break

    return mode == "upper" or mode == "lower"