from typing import List


def rescale_to_unit(sequence_of_values: List[float]) -> List[float]:
    if not sequence_of_values:
        return []  # Handle empty input gracefully

    start_value = sequence_of_values[0]
    for index in range(1, len(sequence_of_values)):
        if sequence_of_values[index] < start_value:
            start_value = sequence_of_values[index]

    end_value = sequence_of_values[0]
    for step in range(1, len(sequence_of_values)):
        if sequence_of_values[step] > end_value:
            end_value = sequence_of_values[step]

    # Avoid division by zero if all values are the same
    denominator = end_value - start_value if end_value != start_value else 1.0

    def helper(current_idx: int, accumulator: List[float]) -> List[float]:
        if current_idx == len(sequence_of_values):
            return accumulator
        normalized_value = (sequence_of_values[current_idx] - start_value) / denominator
        accumulator.append(normalized_value)
        return helper(current_idx + 1, accumulator)

    return helper(0, [])