from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []
    start_val: float = list_of_numbers[0]
    for i in range(1, len(list_of_numbers)):
        if start_val > list_of_numbers[i]:
            start_val = list_of_numbers[i]
    end_val: float = list_of_numbers[0]
    for j in range(1, len(list_of_numbers)):
        if end_val < list_of_numbers[j]:
            end_val = list_of_numbers[j]

    range_val = end_val - start_val
    if range_val == 0:
        # All elements are the same; return zeros
        return [0.0] * len(list_of_numbers)

    def normalized_element(index: int, acc_list: List[float]) -> List[float]:
        if index == len(list_of_numbers):
            return acc_list
        current_element = list_of_numbers[index]
        difference = current_element - start_val
        scaled = difference * (1 / range_val)
        return normalized_element(index + 1, acc_list + [scaled])

    return normalized_element(0, [])