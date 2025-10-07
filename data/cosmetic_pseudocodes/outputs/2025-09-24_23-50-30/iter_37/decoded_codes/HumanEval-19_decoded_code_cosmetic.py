from typing import Dict

def sort_numbers(alpha_str: str) -> str:
    digits_lookup: Dict[str, int] = {
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
    tokens = [tok for tok in alpha_str.split(' ') if tok]
    sorted_tokens = sorted(tokens, key=lambda a: digits_lookup[a])
    return ' '.join(sorted_tokens)