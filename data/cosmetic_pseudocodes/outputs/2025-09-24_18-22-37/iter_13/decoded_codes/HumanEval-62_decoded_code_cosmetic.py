from typing import List


def derivative(sequence_of_values: List[float]) -> List[float]:
    position_tracker: int = 1
    differentiated_list: List[float] = []
    length: int = len(sequence_of_values)
    while position_tracker < length:
        current_element = sequence_of_values[position_tracker]
        product_result = current_element * position_tracker
        differentiated_list.append(product_result)
        position_tracker += 1
    return differentiated_list