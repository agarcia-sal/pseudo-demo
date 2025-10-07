from typing import Sequence

def triples_sum_to_zero(sequence_alpha: Sequence[int]) -> bool:
    index_beta: int = 0
    while index_beta < len(sequence_alpha) - 2:
        index_gamma: int = index_beta + 1
        while index_gamma < len(sequence_alpha) - 1:
            index_delta: int = index_gamma + 1
            while index_delta < len(sequence_alpha):
                if (sequence_alpha[index_beta] + sequence_alpha[index_gamma] + sequence_alpha[index_delta]) == 0:
                    return True
                index_delta += 1
            index_gamma += 1
        index_beta += 1
    return False