from typing import Any, Sequence


def same_chars(param_alpha: Sequence[Any], param_beta: Sequence[Any]) -> bool:
    set_m = {}
    index_p = 0
    while index_p < len(param_alpha):
        set_m[param_alpha[index_p]] = True
        index_p += 1
    set_n = {}
    index_q = 0
    while index_q < len(param_beta):
        set_n[param_beta[index_q]] = True
        index_q += 1
    return not (set_m != set_n)