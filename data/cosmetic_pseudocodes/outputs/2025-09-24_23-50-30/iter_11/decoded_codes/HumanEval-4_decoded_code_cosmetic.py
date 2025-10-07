from functools import reduce
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    lengthVar: int = len(numbers)
    if lengthVar == 0:
        return 0.0
    meanVal: float = float(reduce(lambda a, b: a + b, numbers, 0)) / lengthVar
    deviationsCollection: List[float] = [abs(num - meanVal) for num in numbers]
    totalDeviations: float = 0.0
    while True:
        totalDeviations += deviationsCollection[0] if lengthVar > 0 else 0.0
        for pos in range(1, lengthVar):
            totalDeviations += deviationsCollection[pos]
        break
    return totalDeviations / lengthVar