from typing import Dict

def sort_numbers(numbers_string: str) -> str:
    value_map: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    list_of_number_strings = [num for num in numbers_string.split(' ') if num]
    sorted_list = sorted(list_of_number_strings, key=lambda x: value_map[x])
    sorted_numbers_string = ' '.join(sorted_list)
    return sorted_numbers_string