from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for num_element in list_of_numbers:
        frequency_map[num_element] = frequency_map.get(num_element, 0) + 1
    for element_key in frequency_map:
        if frequency_map[element_key] > 2:
            return False
    index: int = 1
    while index < len(list_of_numbers):
        if not (list_of_numbers[index - 1] <= list_of_numbers[index]):
            return False
        index += 1
    return True