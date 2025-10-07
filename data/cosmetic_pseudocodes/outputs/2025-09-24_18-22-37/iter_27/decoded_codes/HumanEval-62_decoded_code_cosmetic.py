from typing import List

def derivative(array_of_polynomial_terms: List[float]) -> List[float]:
    result_array: List[float] = []
    current_position: int = 1
    while current_position < len(array_of_polynomial_terms):
        temp_value = array_of_polynomial_terms[current_position] * current_position
        result_array.append(temp_value)
        current_position += 1
    return result_array