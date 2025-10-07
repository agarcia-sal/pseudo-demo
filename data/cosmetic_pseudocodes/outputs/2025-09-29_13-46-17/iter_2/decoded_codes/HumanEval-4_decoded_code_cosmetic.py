from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    def recursive_sum_abs_diff(
        elements: List[float], mean_val: float, index: int, acc: float
    ) -> float:
        if index == len(elements):
            return acc
        current_element = elements[index]
        updated_acc = acc + abs(current_element - mean_val)
        return recursive_sum_abs_diff(elements, mean_val, index + 1, updated_acc)

    total_sum = 0.0
    idx = 0
    length = len(list_of_numbers)
    while idx < length:
        total_sum += list_of_numbers[idx]
        idx += 1

    mean_value = total_sum / length
    sum_abs_deviation = recursive_sum_abs_diff(list_of_numbers, mean_value, 0, 0.0)
    mad_result = sum_abs_deviation / length
    return mad_result