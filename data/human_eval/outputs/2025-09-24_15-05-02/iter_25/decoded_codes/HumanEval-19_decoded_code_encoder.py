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
    split_list = numbers_string.split(' ')
    filtered_list = [x for x in split_list if x]
    sorted_list = sorted(filtered_list, key=lambda x: value_map[x])
    return ' '.join(sorted_list)