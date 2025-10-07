from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    mode: str = "start"
    index: int = 0
    keys_list = list(dictionary.keys())
    while index < len(keys_list):
        current_key = keys_list[index]

        if not isinstance(current_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if current_key.isupper():
                mode = "upper"
            elif current_key.islower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and not current_key.isupper()) or (mode == "lower" and not current_key.islower()):
            mode = "mixed"
            break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"