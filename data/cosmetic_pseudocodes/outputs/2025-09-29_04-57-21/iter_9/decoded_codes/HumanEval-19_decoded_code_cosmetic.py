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
        'nine': 9
    }
    tokens = [token for token in string_of_number_words.split(" ") if token != ""]
    index = 0
    while index + 1 < len(tokens):
        position = index + 1
        while position > 0 and digit_values[tokens[position - 1]] > digit_values[tokens[position]]:
            tokens[position - 1], tokens[position] = tokens[position], tokens[position - 1]
            position -= 1
        index += 1
    return " ".join(tokens)