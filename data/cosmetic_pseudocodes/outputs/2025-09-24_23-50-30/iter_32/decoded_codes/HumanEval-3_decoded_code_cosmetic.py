from typing import List

def below_zero(array_of_changes: List[int]) -> bool:
    index: int = 0
    accumulator: int = 0
    length: int = len(array_of_changes)
    while index < length:
        accumulator += array_of_changes[index]
        if accumulator < 0:
            return True
        index += 1
    return False