from typing import Dict, Any


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    current_state: str = "start"
    keys_list = list(dictionary.keys())
    index: int = 0

    while index < len(keys_list):
        k = keys_list[index]
        if not isinstance(k, str):
            current_state = "mixed"
            break

        if current_state == "start":
            if not k.islower() and k.isupper():
                current_state = "upper"
            elif not k.isupper() and k.islower():
                current_state = "lower"
            else:
                break
        elif current_state == "upper":
            if not k.isupper():
                current_state = "mixed"
                break
        elif current_state == "lower":
            if not k.islower():
                current_state = "mixed"
                break
        else:
            break

        index += 1

    return current_state == "upper" or current_state == "lower"