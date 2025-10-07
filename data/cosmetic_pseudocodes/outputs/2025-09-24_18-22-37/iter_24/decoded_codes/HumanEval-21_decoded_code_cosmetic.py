from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    if not sequence_of_values:
        return []

    smallest_element = sequence_of_values[0]
    highest_element = sequence_of_values[0]
    cursor1 = 1

    while cursor1 < len(sequence_of_values):
        current_val = sequence_of_values[cursor1]
        if current_val < smallest_element:
            smallest_element = current_val
        elif current_val > highest_element:
            highest_element = current_val
        cursor1 += 1

    adjusted_range = highest_element - smallest_element
    if adjusted_range == 0:
        # All values are equal; normalized values should be zero to avoid division by zero
        return [0.0 for _ in sequence_of_values]

    result_list: List[float] = []
    idx = 0
    while idx < len(sequence_of_values):
        val_to_transform = sequence_of_values[idx]
        shifted_val = val_to_transform - smallest_element
        scaled_val = shifted_val / adjusted_range
        result_list.append(scaled_val)
        idx += 1

    return result_list