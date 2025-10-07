from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    if not sequence_of_values:
        return []

    least_value = sequence_of_values[0]
    index_var = 1
    while index_var < len(sequence_of_values):
        if sequence_of_values[index_var] < least_value:
            least_value = sequence_of_values[index_var]
        index_var += 1

    greatest_value = sequence_of_values[0]
    position_var = 1
    while position_var < len(sequence_of_values):
        if greatest_value < sequence_of_values[position_var]:
            greatest_value = sequence_of_values[position_var]
        position_var += 1

    range_diff = greatest_value - least_value
    if range_diff == 0:
        # Avoid division by zero: all values are equal, return zeros
        return [0.0 for _ in sequence_of_values]

    result_collection: List[float] = []
    iterator_var = 0
    while iterator_var < len(sequence_of_values):
        temp_var = sequence_of_values[iterator_var] - least_value
        scaled_var = temp_var / range_diff
        result_collection.append(scaled_var)
        iterator_var += 1

    return result_collection