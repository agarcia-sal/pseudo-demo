from typing import Set

def same_chars(str_alpha: str, str_beta: str) -> bool:
    set_a: Set[str] = set()
    idx_a: int = 0
    while idx_a < len(str_alpha):
        set_a.add(str_alpha[idx_a])
        idx_a += 1

    set_b: Set[str] = set()
    pos_b: int = 0
    while pos_b < len(str_beta):
        set_b.add(str_beta[pos_b])
        pos_b += 1

    result_flag: bool = False
    if not (set_a != set_b):
        result_flag = True

    return result_flag