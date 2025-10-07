from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    histogram = {key: 0 for key in list_of_numbers}
    pointer = 0
    while pointer < len(list_of_numbers):
        element = list_of_numbers[pointer]
        prior_count = histogram[element]
        histogram[element] = prior_count + 1
        pointer += 1

    flag_excess = False
    iterator_index = 0
    while iterator_index < len(list_of_numbers) and not flag_excess:
        current_key = list_of_numbers[iterator_index]
        frequency = histogram[current_key]
        if frequency > 2:
            flag_excess = True
            break
        iterator_index += 1

    if flag_excess:
        return False

    position = 1
    is_non_decreasing = True
    while position < len(list_of_numbers) and is_non_decreasing:
        prior_value = list_of_numbers[position - 1]
        current_value = list_of_numbers[position]
        if prior_value > current_value:
            is_non_decreasing = False
            break
        position += 1

    if is_non_decreasing:
        return True
    else:
        return False