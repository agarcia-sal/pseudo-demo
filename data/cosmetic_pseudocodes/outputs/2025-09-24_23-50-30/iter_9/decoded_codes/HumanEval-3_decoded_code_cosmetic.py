from typing import Iterable

def below_zero(sequence: Iterable[int]) -> bool:
    accumulator: int = 0
    for element in sequence:
        accumulator += element
        if accumulator < 0:
            return True
    return False