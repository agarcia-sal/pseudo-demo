from typing import Sequence, Union

def is_happy(param1: Sequence[Union[str, int]]) -> bool:
    if len(param1) < 3:
        return False

    varA = 0
    limit = len(param1) - 3
    while varA <= limit:
        if param1[varA] == param1[varA + 1]:
            return False
        if param1[varA + 1] == param1[varA + 2]:
            return False
        if param1[varA] == param1[varA + 2]:
            return False
        varA += 1

    return True