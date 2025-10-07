from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    digit_values: dict[str, int] = {
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
    filtered_words: List[str] = [element for element in string_of_number_words.split(' ') if element != '']
    sorted_words: List[str] = sorted(filtered_words, key=lambda element: digit_values[element])
    return ' '.join(sorted_words)