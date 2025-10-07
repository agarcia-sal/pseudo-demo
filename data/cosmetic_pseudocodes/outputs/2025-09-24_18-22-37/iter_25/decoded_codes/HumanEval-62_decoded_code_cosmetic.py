from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    result_collection: List[float] = []
    position_counter: int = 0
    while position_counter < len(sequence_of_values):
        if position_counter != 0:
            current_value = sequence_of_values[position_counter]
            product_value = current_value * position_counter
            result_collection.append(product_value)
        position_counter += 1
    return result_collection