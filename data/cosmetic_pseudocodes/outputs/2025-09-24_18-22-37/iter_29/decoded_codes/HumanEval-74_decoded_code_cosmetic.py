from typing import Sequence, List, Union

def total_match(array_alpha: Sequence[str], array_beta: Sequence[str]) -> Union[Sequence[str], Sequence[str]]:
    sum_beta: int = 0
    idx_beta: int = 0
    while idx_beta < len(array_beta):
        elem_beta: str = array_beta[idx_beta]
        sum_beta += len(elem_beta)
        idx_beta += 1

    sum_alpha: int = 0
    pos_alpha: int = 0
    while pos_alpha < len(array_alpha):
        elem_alpha: str = array_alpha[pos_alpha]
        sum_alpha += len(elem_alpha)
        pos_alpha += 1

    if sum_alpha <= sum_beta:
        return array_alpha
    else:
        return array_beta