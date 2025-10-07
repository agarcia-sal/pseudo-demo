from typing import List

def total_match(array_alpha: List[str], array_beta: List[str]) -> List[str]:
    def accumulate_lengths(sequence: List[str], index: int, accumulator: int) -> int:
        if index >= len(sequence):
            return accumulator
        else:
            return accumulate_lengths(sequence, index + 1, accumulator + len(sequence[index]))

    sum_alpha: int = accumulate_lengths(array_alpha, 0, 0)
    sum_beta: int = accumulate_lengths(array_beta, 0, 0)

    if sum_alpha <= sum_beta:
        return array_alpha
    else:
        return array_beta