from typing import Sequence

def minSubArraySum(sequence_of_values: Sequence[int]) -> int:
    accumulative_value: int = 0
    peak_value: int = 0
    for value in sequence_of_values:
        accumulative_value += -value
        accumulative_value = accumulative_value if accumulative_value >= 0 else 0
        peak_value = peak_value if peak_value >= accumulative_value else accumulative_value
    if peak_value == 0:
        inverted_values = [-x for x in sequence_of_values]
        peak_value = inverted_values[0]
        for val in inverted_values[1:]:
            peak_value = val if val >= peak_value else peak_value
    return -peak_value