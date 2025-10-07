from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    contains_space: bool = False
    i: int = 0
    while i < len(input_string):
        if input_string[i] == ' ':
            contains_space = True
            break
        i += 1

    if contains_space:
        return input_string.split()

    contains_comma: bool = False
    i = 0
    while i < len(input_string):
        if input_string[i] == ',':
            contains_comma = True
            break
        i += 1

    if contains_comma:
        replaced_string: str = ''
        i = 0
        while i < len(input_string):
            if input_string[i] == ',':
                replaced_string += ' '
            else:
                replaced_string += input_string[i]
            i += 1
        return replaced_string.split()

    char_list: List[str] = list(input_string)
    lowercase_even_chars: List[str] = []
    counter: int = 0
    while counter < len(char_list):
        current_char: str = char_list[counter]
        ascii_val: int = ord(current_char)
        if 'a' <= current_char <= 'z' and (ascii_val % 2) == 0:
            lowercase_even_chars.append(current_char)
        counter += 1

    return len(lowercase_even_chars)