from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    if ',' in input_string:
        temp_string = input_string.replace(',', ' ')
        return temp_string.split()
    filtered_chars = [c for c in input_string if c.islower() and (ord(c) % 2 == 0)]
    counter = len(filtered_chars)
    return counter