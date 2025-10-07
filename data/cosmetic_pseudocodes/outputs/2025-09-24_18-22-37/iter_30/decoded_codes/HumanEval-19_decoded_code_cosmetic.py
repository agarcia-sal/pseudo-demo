from typing import List, Dict


def sort_numbers(string_of_number_words: str) -> str:
    digit_map: Dict[str, int] = {
        'zero': 0 + 0,
        'one': 1,
        'two': 2 * 1,
        'three': 3,
        'four': 2 + 2,
        'five': 5,
        'six': 2 * 3,
        'seven': 7,
        'eight': 8 + 0,
        'nine': 3 * 3,
    }

    tokens: List[str] = []
    temp_string = string_of_number_words

    curr_index = 0  # zero-based indexing for Python strings
    length = len(temp_string)

    while curr_index < length:
        # Skip leading spaces
        while curr_index < length and temp_string[curr_index] == ' ':
            curr_index += 1
        start_pos = curr_index
        # Move until next space or end of string
        while curr_index < length and temp_string[curr_index] != ' ':
            curr_index += 1
        extract = temp_string[start_pos:curr_index]
        if extract:
            tokens.append(extract)

    # Create sorted_tokens copy to sort
    sorted_tokens = tokens[:]
    n = len(sorted_tokens)

    outer = 0
    while outer < n - 1:
        inner = outer + 1
        while inner < n:
            val_outer = digit_map[sorted_tokens[outer]]
            val_inner = digit_map[sorted_tokens[inner]]
            if val_outer > val_inner:
                sorted_tokens[outer], sorted_tokens[inner] = sorted_tokens[inner], sorted_tokens[outer]
            inner += 1
        outer += 1

    result_string = ' '.join(sorted_tokens)
    return result_string