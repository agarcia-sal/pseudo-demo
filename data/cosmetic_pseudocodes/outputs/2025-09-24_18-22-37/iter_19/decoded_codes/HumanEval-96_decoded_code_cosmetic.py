from typing import List

def count_up_to(number: int) -> List[int]:
    results: List[int] = []
    outerIndex: int = 2
    while outerIndex < number:
        primalityFlag: bool = True
        innerIndex: int = 2
        while True:
            if not (innerIndex < outerIndex):
                break
            remainder: int = outerIndex % innerIndex
            if remainder == 0:
                primalityFlag = False
                break
            innerIndex += 1
        if primalityFlag:
            results.append(outerIndex)
        outerIndex += 1
    return results