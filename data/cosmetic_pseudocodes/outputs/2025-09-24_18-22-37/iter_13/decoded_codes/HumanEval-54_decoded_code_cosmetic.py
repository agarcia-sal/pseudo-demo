from typing import Set

def same_chars(string_alpha: str, string_beta: str) -> bool:
    set_gamma: Set[str] = set()
    set_delta: Set[str] = set()
    idx1: int = 0
    while idx1 < len(string_alpha):
        set_gamma.add(string_alpha[idx1])
        idx1 += 1
    idx2: int = 0
    while True:
        set_delta.add(string_beta[idx2])
        idx2 += 1
        if idx2 >= len(string_beta):
            break
    return set_gamma == set_delta