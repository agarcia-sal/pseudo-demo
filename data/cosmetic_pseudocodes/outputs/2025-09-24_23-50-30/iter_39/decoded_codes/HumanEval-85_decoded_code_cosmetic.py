from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    idx: int = 1
    aggregate: int = 0
    while idx < len(sequence):
        current: int = sequence[idx]
        if current % 2 == 0:
            aggregate += current
        idx += 2
    return aggregate