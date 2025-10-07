from typing import Sequence

def digitSum(inputSequence: Sequence[str]) -> int:
    totalValue: int = 0
    index: int = 0
    while index < len(inputSequence):
        ch = inputSequence[index]
        currentValue: int = ord(ch) if 'A' <= ch <= 'Z' else 0
        totalValue += currentValue
        index += 1
    return totalValue