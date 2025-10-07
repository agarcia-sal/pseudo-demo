from typing import Sequence

def mean_absolute_deviation(sequence_container: Sequence[float]) -> float:
    count_tracker: int = 0
    aggregate_sum: float = 0.0
    for element in sequence_container:
        aggregate_sum += element
        count_tracker += 1

    if count_tracker == 0:
        raise ValueError("sequence_container must not be empty")

    central_tendency: float = aggregate_sum / count_tracker

    def compute_deviation(index: int, current_cumulative: float) -> float:
        if index == count_tracker:
            return current_cumulative
        else:
            return compute_deviation(
                index + 1,
                current_cumulative + abs(sequence_container[index] - central_tendency),
            )

    cumulative_dev: float = compute_deviation(0, 0.0)
    return cumulative_dev / count_tracker