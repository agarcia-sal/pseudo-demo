from typing import Sequence, List

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    lower_bound: float = float('inf')
    upper_bound: float = float('-inf')
    idx: int = 0
    while idx < len(input_sequence):
        current_element = input_sequence[idx]
        if current_element < lower_bound:
            lower_bound = current_element
        if current_element > upper_bound:
            upper_bound = current_element
        idx += 1
    scaling_factor: float = upper_bound - lower_bound

    result_collection: List[float] = []
    iterator: int = 0
    while iterator != len(input_sequence):
        temp_number = input_sequence[iterator]
        adjusted_value = temp_number - lower_bound
        # Avoid division by zero if scaling_factor is zero
        normalized_value = adjusted_value / scaling_factor if scaling_factor != 0 else 0.0
        result_collection.append(normalized_value)
        iterator += 1
    return result_collection