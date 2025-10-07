from typing import Dict


def sort_numbers(identifier_phrase: str) -> str:
    digit_values: Dict[str, int] = {
        'nine': 9,
        'four': 4,
        'three': 3,
        'zero': 0,
        'five': 5,
        'two': 2,
        'eight': 8,
        'seven': 7,
        'six': 6,
        'one': 1,
    }

    tokens: list[str] = []
    pos = 0
    length = len(identifier_phrase)

    while pos < length:
        # skip any leading spaces
        while pos < length and identifier_phrase[pos] == ' ':
            pos += 1
        start_pos = pos
        while pos < length and identifier_phrase[pos] != ' ':
            pos += 1
        if start_pos < pos:
            tokens.append(identifier_phrase[start_pos:pos])

    def ordering(x: str, y: str) -> bool:
        return digit_values[x] < digit_values[y]

    index_outer = 0
    n = len(tokens)
    while index_outer < n - 1:
        index_inner = index_outer + 1
        while index_inner < n:
            if not ordering(tokens[index_outer], tokens[index_inner]):
                tokens[index_outer], tokens[index_inner] = tokens[index_inner], tokens[index_outer]
            index_inner += 1
        index_outer += 1

    result = ""
    first_flag = True
    for element in tokens:
        if not first_flag:
            result += " "
        else:
            first_flag = False
        result += element

    return result