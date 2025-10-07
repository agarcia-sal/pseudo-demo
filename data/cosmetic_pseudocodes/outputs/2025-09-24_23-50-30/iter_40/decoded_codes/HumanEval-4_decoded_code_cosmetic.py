from typing import Sequence
from functools import reduce

def mean_absolute_deviation(input_sequence: Sequence[float]) -> float:
    length = len(input_sequence)
    if length == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")
    intermediate_mean = reduce(lambda acc, el: acc + el, input_sequence, 0) / length
    cumulative_deviation = reduce(lambda acc, val: acc + abs(val - intermediate_mean), input_sequence, 0)
    result_deviation = cumulative_deviation / length
    return result_deviation