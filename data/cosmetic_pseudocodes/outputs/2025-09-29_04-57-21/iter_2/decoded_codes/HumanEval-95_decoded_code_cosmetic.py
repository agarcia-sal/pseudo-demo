from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) <= 0:
        return False

    mode: str = "start"
    for item_key in dictionary.keys():
        if not isinstance(item_key, str):
            mode = "mixed"
            break

        if mode == "start":
            if item_key == item_key.upper():
                mode = "upper"
            elif item_key == item_key.lower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and item_key != item_key.upper()) or (mode == "lower" and item_key != item_key.lower()):
            mode = "mixed"
            break
        else:
            break

    return mode == "upper" or mode == "lower"