from typing import Iterable

def same_chars(param_alpha: Iterable[str], param_beta: Iterable[str]) -> bool:
    assembled_x = set(param_alpha)
    assembled_y = set(param_beta)
    return assembled_x == assembled_y