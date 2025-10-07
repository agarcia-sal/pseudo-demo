from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    contains_space: bool = False
    for ch in input_string:
        if ch == ' ':
            contains_space = True
            break

    if contains_space:
        return input_string.split()

    contains_comma: bool = False
    for ch in input_string:
        if ch == ',':
            contains_comma = True
            break

    if contains_comma:
        transformed_string = ''.join(' ' if ch == ',' else ch for ch in input_string)
        return transformed_string.split()

    char_list: List[str] = list(input_string)
    filtered_chars: List[str] = []
    for current_char in char_list:
        ascii_val = ord(current_char)
        if 'a' <= current_char <= 'z':
            if ascii_val % 2 == 0:
                filtered_chars.append(current_char)

    even_lower_count: int = len(filtered_chars)
    return even_lower_count