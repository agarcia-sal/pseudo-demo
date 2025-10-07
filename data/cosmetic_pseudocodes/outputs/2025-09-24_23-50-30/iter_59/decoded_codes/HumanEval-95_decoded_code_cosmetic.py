from collections.abc import Mapping
from typing import Any


def check_dict_case(x1: Mapping[Any, Any]) -> bool:
    keys = list(x1.keys())
    if len(keys) == 0:
        return False

    state: str = "start"
    while keys:
        x3 = keys.pop(0)
        if not isinstance(x3, str):
            state = "mixed"
            break
        if state == "start":
            if x3 == x3.upper() and any(c.isalpha() for c in x3):
                state = "upper"
            elif x3 == x3.lower() and any(c.isalpha() for c in x3):
                state = "lower"
            else:
                break
        else:
            if (state == "upper" and x3 != x3.upper()) or (state == "lower" and x3 != x3.lower()):
                state = "mixed"
                break
            else:
                break

    return state == "upper" or state == "lower"