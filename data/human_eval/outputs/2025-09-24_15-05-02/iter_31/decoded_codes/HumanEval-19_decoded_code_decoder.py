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
    # Filter out any empty strings resulting from split
    list_of_number_words = [word for word in string_of_number_words.split(' ') if word]
    # Sort by the numeric mapping, ignoring words not in value_map
    sorted_list = sorted(
        (word for word in list_of_number_words if word in value_map),
        key=lambda w: value_map[w]
    )
    return ' '.join(sorted_list)