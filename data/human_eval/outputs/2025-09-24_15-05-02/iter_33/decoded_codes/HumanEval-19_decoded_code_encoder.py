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
        'nine': 9,
    }
    list_of_words = string_of_number_words.split(' ')
    filtered_list = [x for x in list_of_words if x]
    sorted_list = sorted(filtered_list, key=lambda x: value_map[x])
    result_string = ' '.join(sorted_list)
    return result_string