from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map = {element: 0 for element in list_of_numbers}
    for element in list_of_numbers:
        frequency_map[element] += 1
    for key in list_of_numbers:
        if frequency_map[key] > 2:
            return False
    index = 1
    while index < len(list_of_numbers):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False
        index += 1
    return True