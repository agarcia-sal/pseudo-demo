from typing import Iterable

def same_chars(var_x1: Iterable[str], var_x2: Iterable[str]) -> bool:
    var_a3 = set()
    for var_b2 in var_x1:
        var_a3 = var_a3.union({var_b2})
    var_c4 = set()
    for var_d5 in var_x2:
        var_c4 = var_c4.union({var_d5})
    if not (var_a3 == var_c4):
        return False
    else:
        return True