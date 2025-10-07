from typing import Set


def same_chars(delta_str: str, omega_str: str) -> bool:
    alpha_set: Set[str] = set()
    beta_set: Set[str] = set()
    i: int = 0
    while i < len(delta_str):
        alpha_set.add(delta_str[i])
        i += 1
    i = 0
    while True:
        if i >= len(omega_str):
            break
        beta_set.add(omega_str[i])
        i += 1
    result: bool
    if alpha_set == beta_set:
        result = True
    else:
        result = False
    return result