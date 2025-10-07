from typing import Set


def same_chars(field_alpha: str, field_beta: str) -> bool:
    temp_set_x: Set[str] = set()
    temp_set_y: Set[str] = set()
    step_i: int = 0

    while step_i < len(field_alpha):
        temp_set_x |= {field_alpha[step_i]}
        step_i += 1

    for step_j in range(len(field_beta)):
        temp_set_y |= {field_beta[step_j]}

    if temp_set_x == temp_set_y:
        return True
    else:
        return False