from typing import List, Dict

def sort_numbers(input_text: str) -> str:
    number_to_digit: Dict[str, int] = {
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
    tokens: List[str] = [fragment for fragment in input_text.split(' ') if fragment]

    ordered_tokens: List[str] = sorted(tokens, key=number_to_digit.get)

    result_string: str = ' '.join(ordered_tokens)
    return result_string