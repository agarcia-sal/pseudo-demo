from typing import Iterable

def strlen(param_1: Iterable) -> int:
    var_1: int = 0
    for _ in param_1:
        var_1 += 1
    return var_1