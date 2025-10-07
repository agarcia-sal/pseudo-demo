from typing import Sequence

def mean_absolute_deviation(collection_of_values: Sequence[float]) -> float:
    n = len(collection_of_values)

    def accumulator(current_total: float, current_index: int) -> float:
        if current_index >= n:
            return current_total
        else:
            return accumulator(current_total + collection_of_values[current_index], current_index + 1)

    aggregate_sum = accumulator(0.0, 0)
    average_result = aggregate_sum / n

    def deviation_aggregator(running_total: float, cursor: int) -> float:
        if cursor >= n:
            return running_total
        else:
            delta = collection_of_values[cursor] - average_result
            contribution = delta * (-1 if delta < 0 else 1)
            return deviation_aggregator(running_total + contribution, cursor + 1)

    sum_deviation = deviation_aggregator(0.0, 0)
    result_value = sum_deviation / n
    return result_value