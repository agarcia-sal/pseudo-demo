from typing import List


def sort_numbers(input_sequence: str) -> str:
    numeric_reference: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 1 + 1,
        'three': (1 + 1) + 1,
        'four': 2 * 2,
        'five': (2 * 2) + 1,
        'six': 3 * 2,
        'seven': (3 * 2) + 1,
        'eight': 4 * 2,
        'nine': (4 * 2) + 1,
    }

    tokens: List[str] = []
    temp_index: int = 0
    length: int = len(input_sequence)

    while temp_index < length:
        current_token = ''
        while temp_index < length and input_sequence[temp_index] != ' ':
            current_token += input_sequence[temp_index]
            temp_index += 1
        if current_token:
            tokens.append(current_token)
        temp_index += 1

    sorted_tokens = tokens.copy()

    for pos in range(len(sorted_tokens)):
        min_pos = pos
        checker = pos + 1
        while checker < len(sorted_tokens):
            if numeric_reference[sorted_tokens[checker]] < numeric_reference[sorted_tokens[min_pos]]:
                min_pos = checker
            checker += 1
        if min_pos != pos:
            sorted_tokens[pos], sorted_tokens[min_pos] = sorted_tokens[min_pos], sorted_tokens[pos]

    output_string = ''
    counter = 0
    while counter < len(sorted_tokens):
        if counter == 0:
            output_string = sorted_tokens[counter]
        else:
            output_string += ' ' + sorted_tokens[counter]
        counter += 1

    return output_string