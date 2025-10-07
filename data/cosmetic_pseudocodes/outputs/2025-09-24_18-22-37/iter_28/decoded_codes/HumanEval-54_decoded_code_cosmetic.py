from typing import Set

def same_chars(param_alpha: str, param_beta: str) -> bool:
    temp_set_x: Set[str] = set()
    temp_set_y: Set[str] = set()

    index_m: int = 0
    length_m: int = len(param_alpha)
    while index_m < length_m:
        temp_set_x.add(param_alpha[index_m])
        index_m += 1

    length_n: int = len(param_beta)
    for index_n in range(length_n):
        temp_set_y.add(param_beta[index_n])

    return temp_set_x == temp_set_y