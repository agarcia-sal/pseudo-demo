from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    def accumulate(index: int, total: int) -> int:
        if index <= len(sequence):
            if sequence[index - 1] % 2 == 0:
                return accumulate(index + 2, total + sequence[index - 1])
            else:
                return accumulate(index + 2, total)
        else:
            return total
    return accumulate(1, 0)