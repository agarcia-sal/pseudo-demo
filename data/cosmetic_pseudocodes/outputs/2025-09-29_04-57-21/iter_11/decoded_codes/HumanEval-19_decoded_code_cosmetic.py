from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    numerals: dict[str, int] = {
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
    tokens: List[str] = [token for token in string_of_number_words.split(' ') if token]
    # Sort tokens by their numerical value ascending
    ordered = sorted(tokens, key=lambda x: numerals[x])
    return ' '.join(ordered)