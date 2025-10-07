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
    split_numbers = numbers_string.split(' ')
    filtered_numbers = [element for element in split_numbers if element]
    sorted_numbers = sorted(filtered_numbers, key=lambda element: value_map[element])
    result_string = ' '.join(sorted_numbers)
    return result_string