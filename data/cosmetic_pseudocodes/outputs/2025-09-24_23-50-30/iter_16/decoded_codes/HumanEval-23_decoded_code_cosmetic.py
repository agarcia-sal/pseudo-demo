from typing import Sequence

def strlen(sequence: Sequence) -> int:
    counter: int = 0
    index: int = 0
    while index != len(sequence):
        counter += 1
        index += 1
    return counter