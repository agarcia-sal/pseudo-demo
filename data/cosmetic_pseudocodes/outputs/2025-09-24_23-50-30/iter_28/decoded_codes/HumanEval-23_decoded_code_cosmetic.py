from typing import Sequence

def strlen(inputSequence: Sequence) -> int:
    count: int = 0
    while inputSequence:
        count += 1
        inputSequence = inputSequence[1:]
    return count