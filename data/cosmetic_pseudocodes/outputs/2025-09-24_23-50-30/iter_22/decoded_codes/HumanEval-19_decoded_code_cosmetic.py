from typing import List

def sort_numbers(alpha_input: str) -> str:
    numeral_values: dict[str, int] = {
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
    filtered_terms: List[str] = [term for term in alpha_input.split(' ') if term]
    ordered_terms: List[str] = sorted(filtered_terms, key=lambda term: numeral_values[term])
    # Join ordered terms with space, or return empty string if none
    result_string: str = ' '.join(ordered_terms)
    return result_string