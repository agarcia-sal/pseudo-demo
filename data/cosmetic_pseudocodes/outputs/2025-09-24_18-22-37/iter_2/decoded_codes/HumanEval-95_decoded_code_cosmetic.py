from typing import Any, Dict


def check_dict_case(dictionary: Dict[Any, Any]) -> bool:
    if len(dictionary) == 0:
        return False

    mode: str = "start"

    for k in dictionary.keys():
        if not isinstance(k, str):
            mode = "mixed"
            break

        if mode == "start":
            if k == k.upper():
                mode = "upper"
            elif k == k.lower():
                mode = "lower"
            else:
                break
        elif (mode == "upper" and k != k.upper()) or (mode == "lower" and k != k.lower()):
            mode = "mixed"
            break
        else:
            break

    return mode == "upper" or mode == "lower"