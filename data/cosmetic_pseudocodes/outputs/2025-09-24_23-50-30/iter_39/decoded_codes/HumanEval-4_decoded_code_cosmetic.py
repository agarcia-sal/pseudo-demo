from typing import Sequence

def mean_absolute_deviation(dataset: Sequence[float]) -> float:
    size: int = len(dataset)
    if size == 0:
        raise ValueError("dataset must not be empty")

    accumulator: float = 0.0
    index: int = 0

    while index < size:
        accumulator += dataset[index]
        index += 1

    avg: float = accumulator / size
    sum_diff: float = 0.0
    pointer: int = 0

    while pointer < size:
        diff: float = dataset[pointer] - avg
        magnitude: float = diff if diff >= 0 else -diff
        sum_diff += magnitude
        pointer += 1

    result: float = sum_diff / size
    return result