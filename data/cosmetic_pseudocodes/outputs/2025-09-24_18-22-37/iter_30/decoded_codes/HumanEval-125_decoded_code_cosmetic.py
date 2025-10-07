from typing import List, Union


def split_words(source: str) -> Union[List[str], int]:
    has_space: bool = False
    has_comma: bool = False

    pos: int = 0
    while pos < len(source):
        current_char: str = source[pos]
        if current_char == ' ':
            has_space = True
        elif current_char == ',':
            has_comma = True
        pos += 1

    if has_space:
        result_list: List[str] = source.split()
        return result_list

    if has_comma:
        temp_string: str = ""
        idx: int = 0
        while idx < len(source):
            ch: str = source[idx]
            if ch == ',':
                temp_string += ' '
            else:
                temp_string += ch
            idx += 1
        tokens: List[str] = temp_string.split()
        return tokens

    tally: int = 0

    i: int = 0
    while i < len(source):
        sample_char: str = source[i]
        ascii_val: int = ord(sample_char)
        is_lowercase: bool = 'a' <= sample_char <= 'z'
        if is_lowercase and (ascii_val % 2) == 0:
            tally += 1
        i += 1

    return tally