from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    if ',' in input_string:
        replaced_string = input_string.replace(',', ' ')
        return replaced_string.split()
    filtered_chars = [c for c in input_string if 'a' <= c <= 'z' and (ord(c) % 2 == 0)]
    return len(filtered_chars)