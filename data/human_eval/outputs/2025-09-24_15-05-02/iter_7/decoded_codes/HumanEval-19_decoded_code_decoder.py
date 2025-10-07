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
    number_words_list = numbers_string.split(' ')
    filtered_list = [word for word in number_words_list if word]
    sorted_list = sorted(filtered_list, key=lambda element: value_map[element])
    result_string = ' '.join(sorted_list)
    return result_string