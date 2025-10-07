from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def iteratively_calculate(index: int, accumulator: List[float]) -> List[float]:
        if index > len(list_of_coefficients) - 1:
            return accumulator
        return iteratively_calculate(index + 1, accumulator + [list_of_coefficients[index] * index])

    return iteratively_calculate(1, [])