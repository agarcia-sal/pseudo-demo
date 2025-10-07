from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    numeric_values: Dict[str, int] = {
        'nine': 9,
        'eight': 8,
        'seven': 7,
        'six': 6,
        'five': 5,
        'four': 4,
        'three': 3,
        'two': 2,
        'one': 1,
        'zero': 0,
    }

    raw_tokens: list[str] = []
    index: int = 1
    length_counter: int = len(string_of_number_words)
    while index <= length_counter:
        current_char: str = string_of_number_words[index - 1]
        if current_char == ' ':
            raw_tokens.append('')
        else:
            if not raw_tokens:
                raw_tokens.append('')
            last_position: int = len(raw_tokens) - 1
            last_string: str = raw_tokens[last_position]
            raw_tokens[last_position] = last_string + current_char
        index += 1

    cleaned_tokens: list[str] = [item for item in raw_tokens if item != '']

    for i in range(len(cleaned_tokens) - 1, 0, -1):
        for j in range(1, i + 1):
            val_a: int = numeric_values[cleaned_tokens[j - 1]]
            val_b: int = numeric_values[cleaned_tokens[j]]
            if val_a > val_b:
                cleaned_tokens[j - 1], cleaned_tokens[j] = cleaned_tokens[j], cleaned_tokens[j - 1]

    result_string = ''
    for k in range(len(cleaned_tokens) - 1):
        result_string += cleaned_tokens[k] + ' '
    if cleaned_tokens:
        result_string += cleaned_tokens[-1]

    return result_string