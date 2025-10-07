from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count_elements: int = len(list_of_numbers)
    if count_elements == 0:
        return 0.0  # handle empty list gracefully
    average: float = sum(list_of_numbers) / count_elements

    def accumulate_deviation(index: int, acc: float) -> float:
        if index >= count_elements:
            return acc
        current_diff = list_of_numbers[index] - average
        updated_acc = acc + (-current_diff if current_diff < 0 else current_diff)
        return accumulate_deviation(index + 1, updated_acc)

    total_deviation = accumulate_deviation(0, 0.0)
    return total_deviation / count_elements