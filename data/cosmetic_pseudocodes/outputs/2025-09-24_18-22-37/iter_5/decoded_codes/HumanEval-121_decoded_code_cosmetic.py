from typing import Sequence

def solution(sequence: Sequence[int]) -> int:
    totalSum: int = 0
    indexCounter: int = 0
    while indexCounter < len(sequence):
        if (indexCounter % 2) != 0:
            indexCounter += 1
            continue
        elementValue: int = sequence[indexCounter]
        if elementValue % 2 == 1:
            totalSum += elementValue
        indexCounter += 1
    return totalSum