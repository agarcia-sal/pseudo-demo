from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    resulting_list: List[float] = []
    position: int = 1
    while position < len(list_of_coefficients):
        current_value: float = list_of_coefficients[position]
        resulting_list.append(current_value * position)
        position += 1
    return resulting_list