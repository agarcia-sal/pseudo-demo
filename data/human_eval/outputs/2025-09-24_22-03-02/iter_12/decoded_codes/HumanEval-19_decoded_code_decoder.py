from typing import List

def sort_numbers(numbers: str) -> str:
    value_map = {
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
    split_numbers: List[str] = numbers.split(' ')
    filtered_numbers: List[str] = [x for x in split_numbers if x != '']
    sorted_numbers: List[str] = sorted(filtered_numbers, key=lambda x: value_map[x])
    result: str = ' '.join(sorted_numbers)
    return result