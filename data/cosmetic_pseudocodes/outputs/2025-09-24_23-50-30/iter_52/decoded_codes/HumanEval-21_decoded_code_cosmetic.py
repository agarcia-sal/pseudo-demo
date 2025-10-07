from typing import List

def rescale_to_unit(sequence_of_values: List[float]) -> List[float]:
    minimum_value: float = sequence_of_values[0]
    maximum_value: float = sequence_of_values[0]

    for position in range(1, len(sequence_of_values)):
        value = sequence_of_values[position]
        if value < minimum_value:
            minimum_value = value
        elif not (value < maximum_value):
            maximum_value = value

    delta = maximum_value - minimum_value

    def helper_normalize(current_index: int, accumulator: List[float]) -> List[float]:
        if current_index >= len(sequence_of_values):
            return accumulator
        normalized_value = (sequence_of_values[current_index] - minimum_value) / delta  # delta guaranteed nonzero due to min,max from data
        return helper_normalize(current_index + 1, accumulator + [normalized_value])

    return helper_normalize(0, [])