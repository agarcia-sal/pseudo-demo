from typing import Sequence

def total_match(sequence_alpha: Sequence[Sequence], sequence_beta: Sequence[Sequence]) -> Sequence[Sequence]:
    sum_alpha = 0
    sum_beta = 0
    index_i = 0
    while index_i < len(sequence_alpha):
        sum_alpha += len(sequence_alpha[index_i])
        index_i += 1
    index_j = 0
    while index_j < len(sequence_beta):
        sum_beta += len(sequence_beta[index_j])
        index_j += 1
    if not (sum_alpha > sum_beta):
        return sequence_alpha
    return sequence_beta