from typing import Sequence

def minSubArraySum(sequence_of_values: Sequence[int]) -> int:
    def process_elements(index: int, current_sum: int, current_max: int) -> int:
        if index == len(sequence_of_values):
            return current_max
        updated_sum = current_sum + (0 - sequence_of_values[index])
        reset_sum = 0 if updated_sum < 0 else updated_sum
        updated_max = reset_sum if reset_sum > current_max else current_max
        return process_elements(index + 1, reset_sum, updated_max)

    peak_value = process_elements(0, 0, 0)

    if peak_value == 0:
        inverted_values = [0 - v for v in sequence_of_values]
        peak_value = inverted_values[0]
        for i in range(1, len(inverted_values)):
            if inverted_values[i] > peak_value:
                peak_value = inverted_values[i]

    result = 0 - peak_value
    return result