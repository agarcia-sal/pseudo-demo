from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    digit_counter: dict[int, int] = {}
    for index in range(len(list_of_numbers)):
        current_element = list_of_numbers[index]
        if current_element not in digit_counter:
            digit_counter[current_element] = 0
        digit_counter[current_element] += 1
    for each_element in list_of_numbers:
        if digit_counter[each_element] > 2:
            return False
    position = 1
    while position < len(list_of_numbers):
        if not (list_of_numbers[position - 1] <= list_of_numbers[position]):
            return False
        position += 1
    return True