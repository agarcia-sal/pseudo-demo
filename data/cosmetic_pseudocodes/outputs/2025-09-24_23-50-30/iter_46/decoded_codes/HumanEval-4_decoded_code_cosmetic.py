from typing import Sequence

def mean_absolute_deviation(number_collection: Sequence[float]) -> float:
    def accumulate_absolute_differences(items: Sequence[float], center: float, idx: int, acc: float) -> float:
        if idx >= len(items):
            return acc
        else:
            return accumulate_absolute_differences(items, center, idx + 1, acc + abs(items[idx] - center))

    if not number_collection:
        raise ValueError("number_collection must not be empty")

    computed_mean = sum(number_collection) / len(number_collection)
    total_deviation = accumulate_absolute_differences(number_collection, computed_mean, 0, 0.0)
    mad_result = total_deviation / len(number_collection)
    return mad_result