from typing import Sequence

def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    count_elements: int = len(sequence_of_values)
    if count_elements == 0:
        raise ValueError("sequence_of_values must not be empty")
    average_result: float = sum(sequence_of_values) / count_elements
    deviations_collection = [abs(element - average_result) for element in sequence_of_values]
    combined_deviation: float = sum(deviations_collection)
    final_result: float = combined_deviation / count_elements
    return final_result