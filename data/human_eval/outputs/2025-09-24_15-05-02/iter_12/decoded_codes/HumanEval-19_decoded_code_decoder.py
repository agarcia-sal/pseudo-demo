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
        'nine': 9
    }
    words_list = numbers_string.split(' ')
    filtered_words = [word for word in words_list if word]
    sorted_words = sorted(filtered_words, key=lambda word: value_map[word])
    return ' '.join(sorted_words)