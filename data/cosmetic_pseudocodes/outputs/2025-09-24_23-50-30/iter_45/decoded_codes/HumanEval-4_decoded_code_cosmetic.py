from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    quantity: int = len(sequence_of_values)
    if quantity == 0:
        raise ValueError("sequence_of_values must not be empty")
    aggregate_sum: float = 0.0
    index: int = 0
    while index < quantity:
        aggregate_sum += sequence_of_values[index]
        index += 1
    average_value: float = aggregate_sum / quantity

    sum_deviation: float = 0.0
    iterator: int = 0
    while True:
        if iterator >= quantity:
            break
        delta: float = sequence_of_values[iterator] - average_value
        absolute_delta: float = delta if delta >= 0 else -delta
        sum_deviation += absolute_delta
        iterator += 1

    result_to_return: float = sum_deviation / quantity

    return result_to_return