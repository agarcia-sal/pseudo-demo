from typing import Sequence

def smallest_change(numbers: Sequence[int]) -> int:
    tempCount: int = 0
    counterA: int = 0
    limit: int = (len(numbers) // 2) - 1
    while counterA <= limit:
        firstVal: int = numbers[counterA]
        oppIndex: int = len(numbers) - counterA - 1
        secondVal: int = numbers[oppIndex]
        if firstVal != secondVal:
            tempCount += 1
        counterA += 1
    return tempCount