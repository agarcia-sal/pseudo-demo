from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    frequency_map: dict[int, int] = {}
    for element in list_of_numbers:
        frequency_map[element] = frequency_map.get(element, 0) + 1

    for current_value in list_of_numbers:
        if frequency_map[current_value] > 2:
            return False

    position = 1
    is_non_decreasing = True
    length = len(list_of_numbers)
    while position < length and is_non_decreasing:
        previous_element = list_of_numbers[position - 1]
        current_element = list_of_numbers[position]

        if previous_element > current_element:
            is_non_decreasing = False
        else:
            position += 1

    return is_non_decreasing