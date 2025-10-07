from functools import reduce
from typing import Sequence

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    count_elements: int = len(sequence)
    if count_elements == 0:
        return 0.0
    average: float = reduce(lambda acc, val: acc + val, sequence, 0) / count_elements
    summed_deviation: float = reduce(
        lambda accum, elem: accum + (elem - average if elem >= average else average - elem), 
        sequence, 
        0
    )
    return summed_deviation / count_elements