from typing import Dict

def sort_numbers(input_string: str) -> str:
    digit_values: Dict[str, int] = {
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

    temporary_array = input_string.split(' ')
    filtered_array = [word for word in temporary_array if word != '']

    sorted_words = sorted(filtered_array, key=lambda word: digit_values[word])

    return ' '.join(sorted_words)