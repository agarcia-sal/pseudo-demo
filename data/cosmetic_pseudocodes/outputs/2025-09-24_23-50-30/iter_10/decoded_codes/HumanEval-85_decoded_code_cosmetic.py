from typing import Sequence

def add(seq: Sequence[int]) -> int:
    acc: int = 0
    idx: int = 1  # 1-based index per pseudocode

    while idx <= len(seq):
        # Adjust index for 0-based indexing in Python
        if seq[idx - 1] % 2 == 0:
            acc += seq[idx - 1]
        idx += 2

    return acc