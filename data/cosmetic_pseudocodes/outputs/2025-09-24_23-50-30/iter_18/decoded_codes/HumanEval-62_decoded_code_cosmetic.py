from typing import List

def derivative(list_of_coefficients: List[int]) -> List[int]:
    result_list: List[int] = []
    position: int = 1
    while position < len(list_of_coefficients):
        result_list.append(list_of_coefficients[position] * position)
        position += 1
    return result_list