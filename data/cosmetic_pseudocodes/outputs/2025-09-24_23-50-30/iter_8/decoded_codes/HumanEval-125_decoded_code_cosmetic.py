from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    contains_spaces: bool = False
    contains_commas: bool = False

    for char in text:
        if char == ' ':
            contains_spaces = True
            break
    if contains_spaces:
        return text.split()

    for char in text:
        if char == ',':
            contains_commas = True
            break
    if contains_commas:
        replaced_string = ''.join(' ' if ch == ',' else ch for ch in text)
        return replaced_string.split()

    total_lower_even: int = 0
    i: int = 0
    while i < len(text):
        current_char = text[i]
        if 'a' <= current_char <= 'z':
            ascii_val = ord(current_char)
            if ascii_val % 2 == 0:
                total_lower_even += 1
        i += 1

    return total_lower_even