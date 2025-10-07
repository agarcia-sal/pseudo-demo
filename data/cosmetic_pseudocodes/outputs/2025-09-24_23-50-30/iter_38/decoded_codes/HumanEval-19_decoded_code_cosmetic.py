from typing import List

def sort_numbers(token_line: str) -> str:
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
        'nine': 9,
    }
    tokens: List[str] = [word for word in token_line.split(' ') if word != '']
    sorted_tokens: List[str] = sorted(tokens, key=lambda word: digit_values[word])
    return ' '.join(sorted_tokens)