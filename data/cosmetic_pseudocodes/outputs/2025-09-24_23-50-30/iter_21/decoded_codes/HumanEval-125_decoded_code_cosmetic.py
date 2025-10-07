from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    contains_space: bool = False
    for each_char in input_string:
        if each_char == ' ':
            contains_space = True
            break

    if contains_space:
        return input_string.split()

    has_comma: bool = False
    for symbol in input_string:
        if symbol == ',':
            has_comma = True
            break

    if has_comma:
        buffer: List[str] = []
        for element in input_string:
            if element == ',':
                buffer.append(' ')
            else:
                buffer.append(element)
        swapped_string: str = ''.join(buffer)
        return swapped_string.split()
    else:
        char_list: List[str] = list(input_string)
        filtered_chars: List[str] = []
        for ch in char_list:
            if 'a' <= ch <= 'z':
                if ord(ch) % 2 == 0:
                    filtered_chars.append(ch)
        return len(filtered_chars)