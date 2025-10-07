from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
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
    list_of_words = [word for word in string_of_number_words.split(' ') if word]
    sorted_list = sorted(list_of_words, key=value_map.get)
    return ' '.join(sorted_list)