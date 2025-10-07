from typing import Sequence

def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    count: int = len(numbers_collection)
    if count == 0:
        raise ValueError("numbers_collection must not be empty")

    idx: int = 0
    sum_accumulator: float = 0.0
    while idx < count:
        sum_accumulator += numbers_collection[idx]
        idx += 1

    average_value: float = sum_accumulator / count

    def absolute_difference_sum(
        collection: Sequence[float], pivot: float, position: int, accumulator: float
    ) -> float:
        if position == count:
            return accumulator
        deviation = abs(collection[position] - pivot)
        return absolute_difference_sum(collection, pivot, position + 1, accumulator + deviation)

    total_deviation: float = absolute_difference_sum(numbers_collection, average_value, 0, 0.0)

    return total_deviation / count