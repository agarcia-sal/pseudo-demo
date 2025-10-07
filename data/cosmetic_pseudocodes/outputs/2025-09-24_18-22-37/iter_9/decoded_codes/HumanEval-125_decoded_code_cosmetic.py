from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    has_space_found: bool = False
    has_comma_found: bool = False

    for each_char in input_string:
        if each_char == ' ':
            has_space_found = True
        elif each_char == ',':
            has_comma_found = True

    if has_space_found:
        return input_string.split()
    if has_comma_found:
        replaced_string = ''.join(' ' if c == ',' else c for c in input_string)
        return replaced_string.split()

    filtered_characters = [
        letter for letter in input_string
        if 'a' <= letter <= 'z' and (ord(letter) % 2) == 0
    ]
    even_lowercase_count: int = len(filtered_characters)
    return even_lowercase_count