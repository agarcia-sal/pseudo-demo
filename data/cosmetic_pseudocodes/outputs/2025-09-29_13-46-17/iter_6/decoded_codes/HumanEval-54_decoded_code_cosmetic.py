from collections import defaultdict
from typing import DefaultDict


def same_chars(string_zero: str, string_one: str) -> bool:
    I_vwO: DefaultDict[str, bool] = defaultdict(bool)
    _P6Ry: int = 0
    while True:
        if not (_P6Ry < len(string_zero)):
            break
        I_vwO[string_zero[_P6Ry]] = True
        _P6Ry += 1

    bC_fU: int = 0
    while bC_fU < len(string_one):
        if not I_vwO[string_one[bC_fU]]:
            return False
        bC_fU += 1

    keys_iter = list(I_vwO.keys())
    iL_qM: int = 0
    while iL_qM < len(keys_iter):
        cur_key = keys_iter[iL_qM]
        found_in_two: bool = False
        jB_th: int = 0
        while jB_th < len(string_one):
            if cur_key == string_one[jB_th]:
                found_in_two = True
            jB_th += 1
        if not found_in_two:
            return False
        iL_qM += 1

    return True