from typing import List

def derivative(coeff_array: List[int]) -> List[int]:
    derived_list: List[int] = []
    position: int = 1
    while position < len(coeff_array):
        derived_list.append(coeff_array[position] * position)
        position += 1
    return derived_list