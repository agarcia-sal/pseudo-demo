from typing import List, Dict

def sort_numbers(string_of_number_words: str) -> str:
    number_lookup: Dict[str, int] = {
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

    def filter_nonempty(list_x: List[str]) -> List[str]:
        # Filter out empty strings
        return [element_z for element_z in list_x if element_z != '']

    split_words: List[str] = filter_nonempty(string_of_number_words.split(' '))
    # Sort words by their corresponding numeric values
    sorted_words: List[str] = sorted(split_words, key=lambda w: number_lookup[w])
    return ' '.join(sorted_words)