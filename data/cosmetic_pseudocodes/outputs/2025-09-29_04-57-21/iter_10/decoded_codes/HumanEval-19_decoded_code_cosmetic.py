from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
    numeral_values: Dict[str, int] = {
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
    index: int = 0
    length: int = len(string_of_number_words)

    while index < length:
        start_pos = index
        while index < length and string_of_number_words[index] != ' ':
            index += 1
        if index > start_pos:
            tokens.append(string_of_number_words[start_pos:index])
        index += 1

    def compare_by_value(a: str, b: str) -> int:
        return numeral_values[a] - numeral_values[b]

    i: int = 1
    while i < len(tokens):
        j = i
        while j > 0 and compare_by_value(tokens[j], tokens[j - 1]) < 0:
            tokens[j], tokens[j - 1] = tokens[j - 1], tokens[j]
            j -= 1
        i += 1

    result_string = ""
    first_token = True
    for element in tokens:
        if not first_token:
            result_string += " "
        result_string += element
        first_token = False

    return result_string