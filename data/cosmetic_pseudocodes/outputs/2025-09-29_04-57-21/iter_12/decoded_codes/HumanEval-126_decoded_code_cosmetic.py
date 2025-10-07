from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    digit_counts: Dict[int, int] = {}
    index: int = 0
    while index < len(list_of_numbers):
        key = list_of_numbers[index]
        if key not in digit_counts:
            digit_counts[key] = 0
        digit_counts[key] += 1
        index += 1

    for element_key in digit_counts:
        if digit_counts[element_key] > 2:
            return False

    position: int = 1
    while position < len(list_of_numbers):
        if list_of_numbers[position - 1] > list_of_numbers[position]:
            return False
        position += 1

    return True