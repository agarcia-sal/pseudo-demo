from typing import List
from collections import defaultdict


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = defaultdict(int)
    index_var = 0
    while index_var < len(list_of_numbers):
        current_element_var = list_of_numbers[index_var]
        frequency_map[current_element_var] += 1
        index_var += 1

    iterator_var = 0
    while iterator_var < len(list_of_numbers):
        if frequency_map[list_of_numbers[iterator_var]] > 2:
            return False
        iterator_var += 1

    pointer_var = 1
    while pointer_var < len(list_of_numbers):
        if not (list_of_numbers[pointer_var - 1] <= list_of_numbers[pointer_var]):
            return False
        pointer_var += 1

    return True