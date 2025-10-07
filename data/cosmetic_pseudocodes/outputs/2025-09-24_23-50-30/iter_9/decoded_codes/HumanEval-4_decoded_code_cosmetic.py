from typing import Sequence

def mean_absolute_deviation(numbers_collection: Sequence[float]) -> float:
    length_counter: int = len(numbers_collection)
    if length_counter == 0:
        return 0.0
    aggregate_sum: float = 0.0
    for index in range(length_counter):
        aggregate_sum += numbers_collection[index]
    average_score: float = aggregate_sum * (1 / length_counter)
    deviation_accumulator: float = 0.0
    for element in numbers_collection:
        difference: float = element - average_score
        absolute_difference: float = -difference if difference < 0 else difference
        deviation_accumulator += absolute_difference
    return deviation_accumulator * (1 / length_counter)