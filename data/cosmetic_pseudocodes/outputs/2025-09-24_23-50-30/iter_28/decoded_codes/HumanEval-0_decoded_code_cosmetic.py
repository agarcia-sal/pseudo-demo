from typing import Sequence

def has_close_elements(sequence_alpha: Sequence[int], limit_beta: int) -> bool:
    def scan_pair(i: int, j: int) -> bool:
        if i >= len(sequence_alpha):
            return False
        if j >= len(sequence_alpha):
            return scan_pair(i + 1, 0)
        if i == j:
            return scan_pair(i, j + 1)
        delta = sequence_alpha[j] - sequence_alpha[i]
        gap = abs(delta)
        return (gap < limit_beta) or scan_pair(i, j + 1)
    return scan_pair(0, 0)