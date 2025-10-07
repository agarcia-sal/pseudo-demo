from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def multiplyByIndex(position: int, value: float) -> float:
        return position * value

    def buildDerivative(index: int, coefficients: List[float], result: List[float]) -> List[float]:
        if index == len(coefficients):
            return result
        result.append(multiplyByIndex(index, coefficients[index]))
        return buildDerivative(index + 1, coefficients, result)

    return buildDerivative(1, list_of_coefficients, [])