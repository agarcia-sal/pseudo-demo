from typing import List


def mean_absolute_deviation(numbersList: List[float]) -> float:
    if not numbersList:
        return 0.0

    def sumValues(index: int, accumulatedSum: float) -> float:
        if index == len(numbersList):
            return accumulatedSum
        else:
            return sumValues(index + 1, accumulatedSum + numbersList[index])

    averageVal = sumValues(0, 0.0) / len(numbersList)

    def absoluteDeviationSum(currentIdx: int, deviationAcc: float) -> float:
        if currentIdx == len(numbersList):
            return deviationAcc
        else:
            deviation = numbersList[currentIdx] - averageVal
            positiveDeviation = -deviation if deviation < 0 else deviation
            return absoluteDeviationSum(currentIdx + 1, deviationAcc + positiveDeviation)

    totalDeviation = absoluteDeviationSum(0, 0.0)

    return totalDeviation / len(numbersList)