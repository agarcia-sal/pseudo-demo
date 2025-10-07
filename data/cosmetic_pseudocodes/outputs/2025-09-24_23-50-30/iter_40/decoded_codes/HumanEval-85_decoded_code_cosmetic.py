from typing import Sequence

def add(p_sequence: Sequence[int]) -> int:
    p_result: int = 0
    p_index: int = 1
    while p_index <= len(p_sequence):
        if p_sequence[p_index - 1] % 2 == 0:  # -1 for 0-based indexing
            p_result += p_sequence[p_index - 1]
        p_index += 2
    return p_result