from typing import Sequence

def strlen(inputArray: Sequence[object]) -> int:
    count: int = 0
    while count < len(inputArray):  # avoid IndexError by explicit boundary check
        count += 1
    return count