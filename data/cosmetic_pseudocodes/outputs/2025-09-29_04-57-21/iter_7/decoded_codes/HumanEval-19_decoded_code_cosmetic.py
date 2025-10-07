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
    extracted_terms = [token for token in string_of_number_words.split(' ') if token]
    ordered_terms = sorted(extracted_terms, key=lambda x: digit_values[x])
    return ' '.join(ordered_terms)