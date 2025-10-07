from typing import Sequence

def strlen(inputSequence: Sequence) -> int:
    lengthCount: int = 0
    currentIndex: int = 0

    while True:
        if currentIndex >= len(inputSequence):
            break
        lengthCount += 1
        currentIndex += 1

    return lengthCount