from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    numbers_list: List[int] = []
    parts = string_description.split(" ")
    idx = 0
    while idx < len(parts):
        current_element = parts[idx]
        if current_element.isdigit():
            numeric_value = int(current_element)
            numbers_list.append(numeric_value)
        idx += 1
    sum_of_numbers = 0
    position = 0
    while True:
        if position >= len(numbers_list):
            break
        sum_of_numbers += numbers_list[position]
        position += 1
    return total_number_of_fruits - sum_of_numbers