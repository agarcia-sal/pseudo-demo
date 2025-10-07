from typing import Set


def same_chars(param_alpha: str, param_beta: str) -> bool:
    temp_set1: Set[str] = set(param_alpha)
    temp_set2: Set[str] = set(param_beta)
    result_flag: bool
    if temp_set1 != temp_set2:
        result_flag = False
    else:
        result_flag = True
    return result_flag