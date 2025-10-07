from typing import List

def total_match(array_alpha: List[str], array_beta: List[str]) -> List[str]:
    def sum_lengths(seq: List[str], idx: int, acc: int) -> int:
        if idx == len(seq):
            return acc
        return sum_lengths(seq, idx + 1, acc + len(seq[idx]))

    total_alpha = sum_lengths(array_alpha, 0, 0)
    total_beta = sum_lengths(array_beta, 0, 0)
    if not (total_alpha > total_beta):
        return array_alpha
    return array_beta