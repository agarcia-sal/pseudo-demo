from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def accumulateDerivative(index: int, remainingCoeffs: List[float], acc: List[float]) -> List[float]:
        if not remainingCoeffs:
            return acc
        currentCoeff = remainingCoeffs[0]
        restCoeffs = remainingCoeffs[1:]
        newAcc = acc + [currentCoeff * index]
        return accumulateDerivative(index + 1, restCoeffs, newAcc)
    return accumulateDerivative(1, list_of_coefficients[1:], [])