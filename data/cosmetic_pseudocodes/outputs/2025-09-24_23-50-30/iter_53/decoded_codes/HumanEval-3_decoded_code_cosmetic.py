from typing import Sequence

def below_zero(delta_collection: Sequence[int]) -> bool:
    balance_marker: int = 0
    i: int = 0
    while i < len(delta_collection):
        balance_marker += delta_collection[i]
        if balance_marker < 0:
            return True
        i += 1
    return False