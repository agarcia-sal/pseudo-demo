from typing import Set


def same_chars(input_alpha: str, input_beta: str) -> bool:
    temp_set_A: Set[str] = set()
    temp_set_B: Set[str] = set()
    index_gamma: int = 0

    while index_gamma < len(input_alpha):
        temp_set_A.add(input_alpha[index_gamma])
        index_gamma += 1

    index_gamma = 0

    while index_gamma < len(input_beta):
        temp_set_B.add(input_beta[index_gamma])
        index_gamma += 1

    if temp_set_A != temp_set_B:
        return False
    else:
        return True