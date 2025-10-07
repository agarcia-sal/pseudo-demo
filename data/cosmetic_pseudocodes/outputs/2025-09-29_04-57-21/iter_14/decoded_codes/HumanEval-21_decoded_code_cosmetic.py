from typing import List


def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    smallest_value: float = list_of_numbers[0]
    largest_value: float = list_of_numbers[0]
    index_counter: int = 1

    while index_counter < len(list_of_numbers):
        if not (list_of_numbers[index_counter] < smallest_value):
            if list_of_numbers[index_counter] > largest_value:
                largest_value = list_of_numbers[index_counter]
        else:
            smallest_value = list_of_numbers[index_counter]
        index_counter += 1

    difference_range: float = largest_value + (-smallest_value)
    result_list: List[float] = []
    item_iterator: int = 0

    while item_iterator < len(list_of_numbers):
        normalized = (list_of_numbers[item_iterator] + (-smallest_value)) * (1 / difference_range)
        result_list.append(normalized)
        item_iterator += 1

    return result_list