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
    list_of_words = [word for word in numbers_string.split(' ') if word]
    sorted_words = sorted(list_of_words, key=lambda word: value_map[word])
    result_string = ' '.join(sorted_words)
    return result_string