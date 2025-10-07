from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) <= 0:
        return False

    mode = "start"
    index = 0
    keys_list = list(dictionary.keys())

    while index < len(keys_list):
        item = keys_list[index]
        if not isinstance(item, str):
            mode = "mixed"
            break

        if mode == "start":
            if item == item.upper():
                mode = "upper"
            elif item == item.lower():
                mode = "lower"
            else:
                break
        elif mode == "upper":
            if item != item.upper():
                mode = "mixed"
                break
        elif mode == "lower":
            if item != item.lower():
                mode = "mixed"
                break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"