from typing import List

def smallest_change(arrayOfIntegers: List[int]) -> int:
    answerCount: int = 0
    checkLimit: int = (len(arrayOfIntegers) // 2) - 1
    indexTracker: int = 0

    while indexTracker <= checkLimit:
        frontValue: int = arrayOfIntegers[indexTracker]
        rearValue: int = arrayOfIntegers[len(arrayOfIntegers) - 1 - indexTracker]

        if frontValue != rearValue:
            answerCount += 1

        indexTracker += 1

    return answerCount