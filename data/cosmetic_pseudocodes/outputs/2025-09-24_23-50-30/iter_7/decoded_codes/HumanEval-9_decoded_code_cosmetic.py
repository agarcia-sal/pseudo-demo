from typing import Sequence, List

def rolling_max(sequence_of_values: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    marker: int = -1

    while (marker + 1) < len(sequence_of_values):
        marker += 1
        current_value = sequence_of_values[marker]

        if len(accumulator) == 0:
            leading_value = current_value
        else:
            leading_value = current_value if accumulator[-1] < current_value else accumulator[-1]

        accumulator.append(leading_value)

    return accumulator