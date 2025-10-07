from typing import Sequence


def strlen(inputSequence: Sequence) -> int:
    counter: int = 0
    while counter != len(inputSequence):
        counter += 1
    return counter