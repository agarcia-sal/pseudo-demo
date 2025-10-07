from typing import Sequence

def mean_absolute_deviation(input_sequence: Sequence[float]) -> float:
    mean_accumulator: float = 0.0
    total_abs_dev: float = 0.0
    sequence_length: int = len(input_sequence)
    current_index: int = 0

    while current_index < sequence_length:
        mean_accumulator += input_sequence[current_index]
        current_index += 1
    mean_accumulator /= sequence_length

    current_index = 0
    while current_index < sequence_length:
        temp_difference: float = input_sequence[current_index] - mean_accumulator
        temp_abs: float = temp_difference if temp_difference >= 0 else -temp_difference
        total_abs_dev += temp_abs
        current_index += 1

    result_value: float = total_abs_dev / sequence_length

    return result_value