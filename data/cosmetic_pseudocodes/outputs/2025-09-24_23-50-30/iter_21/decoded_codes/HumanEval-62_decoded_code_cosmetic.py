from typing import List

def derivative(coefficients_array: List[float]) -> List[float]:
    result_sequence: List[float] = []
    position_counter: int = 1
    for element_value in coefficients_array[1:]:
        result_sequence.append(element_value * position_counter)
        position_counter += 1
    return result_sequence