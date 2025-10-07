from typing import List

def derivative(sequence_of_values: List[float]) -> List[float]:
    result_collection: List[float] = []
    position_counter: int = 1
    while position_counter < len(sequence_of_values):
        interim_value: float = sequence_of_values[position_counter]
        computed_product: float = interim_value * position_counter
        result_collection.append(computed_product)
        position_counter += 1
    return result_collection