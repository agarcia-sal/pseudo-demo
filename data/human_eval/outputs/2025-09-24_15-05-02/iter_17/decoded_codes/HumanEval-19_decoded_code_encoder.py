from typing import Dict

def sort_numbers(numbers: str) -> str:
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
        'nine': 9
    }

    list_of_words = [x for x in numbers.split(' ') if x]
    sorted_list = sorted(list_of_words, key=lambda x: value_map[x])
    return ' '.join(sorted_list)