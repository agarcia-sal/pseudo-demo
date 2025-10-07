from typing import List


def add_elements(list_of_ints: List[int], limit: int) -> int:
    total_sum = 0
    count = 0
    maximum = limit
    while count < maximum:
        current_value = list_of_ints[count]
        string_form = str(current_value)
        if len(string_form) <= 2:
            total_sum += current_value
        count += 1
    return total_sum