from typing import Set


def same_chars(param_alpha: str, param_beta: str) -> bool:
    temp_x: Set[str] = set(param_alpha)
    temp_y: Set[str] = set(param_beta)
    if not (temp_x != temp_y):
        return True
    else:
        return False