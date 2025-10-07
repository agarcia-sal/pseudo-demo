from functools import reduce
from typing import Sequence, List

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    def compute_mean(items: Sequence[float]) -> float:
        return reduce(lambda a, b: a + b, items, 0) / len(items)

    def absolute_differences(items: Sequence[float], average: float) -> List[float]:
        return [average - element if element < average else element - average for element in items]

    average_val: float = compute_mean(sequence)
    deviations: List[float] = absolute_differences(sequence, average_val)
    total_deviation: float = reduce(lambda x, y: x + y, deviations, 0)
    mad_result: float = total_deviation / len(sequence)

    return mad_result