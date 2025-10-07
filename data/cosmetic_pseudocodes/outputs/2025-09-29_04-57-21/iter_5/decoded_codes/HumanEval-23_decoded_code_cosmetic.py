from typing import Iterable

def strlen(sequence: Iterable) -> int:
    lengthCounter: int = 0
    for _ in sequence:
        lengthCounter += 1
    return lengthCounter