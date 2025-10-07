from typing import Union, List

def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    if ',' in input_string:
        interim_string = input_string.replace(',', ' ')
        return interim_string.split()
    filtered_chars = [c for c in input_string if c.islower() and (ord(c) % 2 == 0)]
    total = len(filtered_chars)
    return total