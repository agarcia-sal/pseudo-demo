from typing import Dict, Any


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if not dictionary:
        return False

    mode: str = "start"
    items = list(dictionary.keys())
    index: int = 0

    while index < len(items):
        current = items[index]

        if not isinstance(current, str):
            mode = "mixed"
            break

        if mode == "start":
            if current == current.upper():
                mode = "upper"
            elif current == current.lower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and current != current.upper()) or (mode == "lower" and current != current.lower()):
            mode = "mixed"
            break
        else:
            break

        index += 1

    return mode == "upper" or mode == "lower"