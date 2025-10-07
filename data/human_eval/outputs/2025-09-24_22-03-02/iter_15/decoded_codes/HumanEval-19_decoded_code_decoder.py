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
    split_numbers = numbers.split(' ')
    filtered_numbers: List[str] = []
    for x in split_numbers:
        if x != '':
            filtered_numbers.append(x)
    sorted_numbers = sorted(filtered_numbers, key=lambda x: value_map[x])
    joined_string = ' '.join(sorted_numbers)
    return joined_string