from typing import Dict

def sort_numbers(input_text: str) -> str:
    map_values: Dict[str, int] = {
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

    tokens = [token for token in input_text.split(' ') if token != '']

    n = len(tokens)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if map_values[tokens[i]] > map_values[tokens[j]]:
                tokens[i], tokens[j] = tokens[j], tokens[i]

    output_string = ' '.join(tokens)
    return output_string