from typing import Sequence

def below_zero(sequence: Sequence[int]) -> bool:
    balance_tracker: int = 0
    index: int = 0
    while index < len(sequence):
        balance_tracker += sequence[index]
        if balance_tracker < 0:
            return True
        index += 1
    return False