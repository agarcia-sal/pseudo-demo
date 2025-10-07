from typing import Sequence, Any

def total_match(array_alpha: Sequence[Sequence[Any]], array_beta: Sequence[Sequence[Any]]) -> Sequence[Sequence[Any]]:
    sum_alpha: int = 0
    sum_beta: int = 0
    for index in range(len(array_alpha)):
        temp_length: int = len(array_alpha[index])
        sum_alpha += temp_length
    for index in range(len(array_beta)):
        temp_length = len(array_beta[index])
        sum_beta += temp_length
    if not (sum_alpha > sum_beta):
        return array_alpha
    return array_beta