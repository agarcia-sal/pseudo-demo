from typing import List, Tuple


def poly(list_of_coefficients: List[float], point: float) -> float:
    def powerSum(coeffs: List[float], idx: int) -> float:
        if idx == len(coeffs):
            return 0.0
        return coeffs[idx] * (point ** idx) + powerSum(coeffs, idx + 1)
    return powerSum(list_of_coefficients, 0)


def find_zero(list_of_coefficients: List[float]) -> float:
    def searchInterval(startVal: float, endVal: float) -> Tuple[float, float]:
        if poly(list_of_coefficients, startVal) * poly(list_of_coefficients, endVal) > 0:
            return searchInterval(startVal * 2.0, endVal * 2.0)
        return startVal, endVal

    def binarySearch(beginVal: float, endVal: float) -> float:
        if (endVal - beginVal) <= 1e-10:
            return beginVal
        midPoint = (beginVal + endVal) / 2.0
        if poly(list_of_coefficients, midPoint) * poly(list_of_coefficients, beginVal) > 0:
            return binarySearch(midPoint, endVal)
        else:
            return binarySearch(beginVal, midPoint)

    startDouble = -1.0
    endDouble = 1.0
    startDouble, endDouble = searchInterval(startDouble, endDouble)
    return binarySearch(startDouble, endDouble)