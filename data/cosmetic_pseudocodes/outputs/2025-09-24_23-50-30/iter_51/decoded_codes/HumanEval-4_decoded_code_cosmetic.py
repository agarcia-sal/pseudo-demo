from typing import Sequence


def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    count_of_elements: int = len(array_of_values)
    if count_of_elements == 0:
        raise ValueError("array_of_values must not be empty")

    aggregate_sum: float = 0.0
    index: int = 0

    while index < count_of_elements:
        aggregate_sum += array_of_values[index]
        index += 1

    average: float = aggregate_sum / count_of_elements

    def recursive_abs_sum(position: int, accumulator: float) -> float:
        if position == count_of_elements:
            return accumulator
        else:
            return recursive_abs_sum(
                position + 1,
                accumulator + abs(array_of_values[position] - average)
            )

    total_deviation: float = recursive_abs_sum(0, 0.0)

    return total_deviation / count_of_elements