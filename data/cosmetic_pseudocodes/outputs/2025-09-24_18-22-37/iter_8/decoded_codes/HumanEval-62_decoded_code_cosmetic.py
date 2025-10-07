from typing import List

def derivative(array_of_coefficients: List[float]) -> List[float]:
    derived_array: List[float] = []
    index_counter: int = 0

    while index_counter < len(array_of_coefficients):
        guard_index = index_counter
        if guard_index != 0:
            intermediate_product = array_of_coefficients[guard_index]
            multiplied_value = intermediate_product * guard_index
            derived_array.append(multiplied_value)
        index_counter += 1

    return derived_array