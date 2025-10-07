from typing import Sequence


def same_chars(alpha_b: Sequence[str], beta_c: Sequence[str]) -> bool:
    temp_set_x: set[str] = set()
    temp_set_y: set[str] = set()
    for i in range(len(alpha_b)):
        if alpha_b[i] not in temp_set_x:
            temp_set_x.add(alpha_b[i])
    for j in range(len(beta_c)):
        if beta_c[j] not in temp_set_y:
            temp_set_y.add(beta_c[j])
    return temp_set_x == temp_set_y