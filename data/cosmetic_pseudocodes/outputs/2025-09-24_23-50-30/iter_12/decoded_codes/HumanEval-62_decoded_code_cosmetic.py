from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    output_list: List[float] = []
    position: int = 1
    while position < len(list_of_coefficients):
        output_list.append(list_of_coefficients[position] * position)
        position += 1
    return output_list