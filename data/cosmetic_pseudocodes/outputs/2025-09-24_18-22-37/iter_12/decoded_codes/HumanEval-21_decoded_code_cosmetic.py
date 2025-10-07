from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    if not sequence_of_values:
        return []
    temp_min: float = sequence_of_values[0]
    for idx in range(1, len(sequence_of_values)):
        if sequence_of_values[idx] < temp_min:
            temp_min = sequence_of_values[idx]
    temp_max: float = sequence_of_values[0]
    for idx2 in range(1, len(sequence_of_values)):
        if temp_max < sequence_of_values[idx2]:
            temp_max = sequence_of_values[idx2]
    divisor: float = temp_max - temp_min
    if divisor == 0:
        # All values are the same -> rescale to 0.0 for all elements
        return [0.0] * len(sequence_of_values)
    output_list: List[float] = []
    counter: int = 0
    while counter < len(sequence_of_values):
        current_element: float = sequence_of_values[counter]
        shifted_value: float = current_element - temp_min
        scaled_value: float = shifted_value / divisor
        output_list.append(scaled_value)
        counter += 1
    return output_list