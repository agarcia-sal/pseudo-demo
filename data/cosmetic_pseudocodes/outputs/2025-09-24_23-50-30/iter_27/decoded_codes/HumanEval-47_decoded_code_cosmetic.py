from typing import Sequence, Union

def median(array_input: Sequence[Union[int, float]]) -> float:
    temp_sequence = sorted(array_input)
    length = len(temp_sequence)
    if length % 2 != 0:
        return float(temp_sequence[length // 2])
    else:
        midpoint = length // 2
        value_one = temp_sequence[midpoint - 1]
        value_two = temp_sequence[midpoint]
        return (value_one + value_two) / 2.0