from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    if not sequence_of_values:
        return []
    lowest_value: float = sequence_of_values[0]
    for each_value in sequence_of_values:
        if each_value < lowest_value:
            lowest_value = each_value
    highest_value: float = sequence_of_values[0]
    for each_value in sequence_of_values:
        if each_value > highest_value:
            highest_value = each_value
    range_diff: float = highest_value - lowest_value
    if range_diff == 0:
        # If all values are the same, return zeros to avoid division by zero.
        return [0.0] * len(sequence_of_values)
    result_sequence: List[float] = [(single_value - lowest_value) / range_diff for single_value in sequence_of_values]
    return result_sequence