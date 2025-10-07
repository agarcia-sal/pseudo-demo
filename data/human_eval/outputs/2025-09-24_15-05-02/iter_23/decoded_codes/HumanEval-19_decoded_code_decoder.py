from typing import Dict, List

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
    words_list: List[str] = numbers_string.split(' ')
    filtered_list: List[str] = [word for word in words_list if word]
    # Sort by mapped integer values, ignoring any word not in value_map (robustness)
    sorted_list: List[str] = sorted(filtered_list, key=lambda word: value_map[word])
    result_string: str = ' '.join(sorted_list)
    return result_string