from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    result_list: List[float] = []
    pos: int = 1
    while pos < len(list_of_coefficients):
        current_value: float = list_of_coefficients[pos]
        multiplied: float = current_value * pos
        result_list.append(multiplied)
        pos += 1
    return result_list