from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    return _compute_MAD(0, 0.0, len(list_of_numbers), list_of_numbers)


def _compute_MAD(idxCounter: int, accSum: float, n: int, numbersCollection: List[float]) -> float:
    if idxCounter == n:
        avgMean = accSum / n
        return _aggregate_abs_dev(0, 0.0, n, avgMean, numbersCollection) / n
    newSumAccum = accSum + numbersCollection[idxCounter]
    return _compute_MAD(idxCounter + 1, newSumAccum, n, numbersCollection)


def _aggregate_abs_dev(position: int, runningTotal: float, size: int, meanVal: float, elems: List[float]) -> float:
    if position >= size:
        return runningTotal
    currentElement = elems[position]
    absDifference = currentElement - meanVal if currentElement >= meanVal else meanVal - currentElement
    return _aggregate_abs_dev(position + 1, runningTotal + absDifference, size, meanVal, elems)