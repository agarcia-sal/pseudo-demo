from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
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

    tokens = [t for t in string_of_number_words.split(' ') if t != '']

    n = len(tokens)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if digit_values[tokens[j]] > digit_values[tokens[j + 1]]:
                tokens[j], tokens[j + 1] = tokens[j + 1], tokens[j]

    result_string = tokens[0] if tokens else ''
    for k in range(1, n):
        result_string += ' ' + tokens[k]

    return result_string