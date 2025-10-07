from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    digit_values: Dict[str, int] = {
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

    tokens: list[str] = []
    for index in range(len(string_of_number_words)):
        current_char = string_of_number_words[index]
        if current_char != ' ':
            if tokens and tokens[-1] != '':
                tokens[-1] += current_char
            else:
                tokens.append(current_char)
        else:
            if not tokens or tokens[-1] != '':
                tokens.append('')
    tokens = [t for t in tokens if t != '']

    def get_value(word: str) -> int:
        return digit_values[word]

    n = len(tokens)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if get_value(tokens[j]) > get_value(tokens[j + 1]):
                tokens[j], tokens[j + 1] = tokens[j + 1], tokens[j]

    result_string = ''
    for k in range(n):
        result_string += tokens[k]
        if k < n - 1:
            result_string += ' '
    return result_string