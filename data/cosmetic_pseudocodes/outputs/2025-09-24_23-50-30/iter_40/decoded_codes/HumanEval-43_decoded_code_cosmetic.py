from typing import List

def pairs_sum_to_zero(values: List[int]) -> bool:
    outerIndex: int = 0
    while outerIndex < len(values):
        currentValue: int = values[outerIndex]
        innerIndex: int = outerIndex + 1
        while innerIndex < len(values):
            if (currentValue + values[innerIndex]) == 0:
                return True
            innerIndex += 1
        outerIndex += 1
    return False