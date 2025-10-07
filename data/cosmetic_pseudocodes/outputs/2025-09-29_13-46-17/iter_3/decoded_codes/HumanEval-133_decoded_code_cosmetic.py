from math import ceil, pow
from typing import List

def sum_squares(listOfNumbers: List[float]) -> float:
    def recursiveSum(index: int, accumulator: float) -> float:
        if index >= len(listOfNumbers):
            return accumulator
        currentValue = listOfNumbers[index]
        squaredValue = pow(ceil(currentValue), 2)
        return recursiveSum(index + 1, accumulator + squaredValue)
    return recursiveSum(0, 0)