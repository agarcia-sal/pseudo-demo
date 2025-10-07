import math
from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    cumulativeSum = 0
    indexCounter = 0
    while indexCounter < len(matrix):
        currentRowSum = 0
        elementIndex = 0
        while elementIndex < len(matrix[indexCounter]):
            currentRowSum += matrix[indexCounter][elementIndex]
            elementIndex += 1
        divisionResult = currentRowSum / limit
        roundedValue = math.ceil(divisionResult)
        cumulativeSum += roundedValue
        indexCounter += 1
    return cumulativeSum