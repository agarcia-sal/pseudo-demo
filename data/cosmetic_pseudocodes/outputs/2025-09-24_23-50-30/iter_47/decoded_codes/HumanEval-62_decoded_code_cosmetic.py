from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    accumulator: List[float] = []
    iterator: int = 1
    while iterator < len(list_of_coefficients):
        computed_value = list_of_coefficients[iterator] * iterator
        accumulator.append(computed_value)
        iterator += 1
    return accumulator