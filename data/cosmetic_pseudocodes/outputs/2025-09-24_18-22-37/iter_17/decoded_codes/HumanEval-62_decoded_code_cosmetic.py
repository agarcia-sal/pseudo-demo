from typing import List

def derivative(coefficient_sequence: List[float]) -> List[float]:
    derived_list: List[float] = []
    for index_counter in range(1, len(coefficient_sequence)):
        current_coefficient = coefficient_sequence[index_counter]
        product_value = current_coefficient * index_counter
        derived_list.append(product_value)
    return derived_list