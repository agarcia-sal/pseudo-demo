from typing import List

def add_elements(list_of_numbers: List[int], count_limit: int) -> int:
    total_sum = 0
    index = 0
    while index < count_limit:
        current_value = list_of_numbers[index]
        string_form = str(current_value)
        length_of_string = len(string_form)
        if length_of_string <= 2:
            total_sum += current_value
        index += 1
    return total_sum