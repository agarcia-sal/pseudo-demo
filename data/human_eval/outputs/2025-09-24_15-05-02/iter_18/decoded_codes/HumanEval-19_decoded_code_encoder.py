from typing import List

def sort_numbers(numbers: str) -> str:
    value_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    tokens: List[str] = numbers.split(' ')
    filtered_tokens: List[str] = [x for x in tokens if x]
    sorted_tokens: List[str] = sorted(filtered_tokens, key=lambda x: value_map[x])
    return ' '.join(sorted_tokens)