from typing import Dict, Any


def check_dict_case(dict_obj: Dict[Any, Any]) -> bool:
    keys = list(dict_obj.keys())

    if len(keys) == 0:
        return False

    mode: str = "start"

    def recur(i: int) -> bool:
        nonlocal mode

        if i == len(keys):
            return mode == "upper" or mode == "lower"

        k = keys[i]

        if not isinstance(k, str):
            mode = "mixed"
            return False

        if mode == "start":
            if k == k.upper():
                mode = "upper"
            elif k == k.lower():
                mode = "lower"
            else:
                mode = "mixed"
                return False
        elif (mode == "upper" and k != k.upper()) or (mode == "lower" and k != k.lower()):
            mode = "mixed"
            return False

        return recur(i + 1)

    return recur(0)