from typing import List

def derivative(array_of_coeffs: List[int]) -> List[int]:
    result_array: List[int] = []
    position: int = 1
    while position < len(array_of_coeffs):
        coeff: int = array_of_coeffs[position]
        product: int = coeff * position
        result_array.append(product)
        position += 1
    return result_array