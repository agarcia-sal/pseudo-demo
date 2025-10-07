from typing import List, Union

def split_words(str: str) -> Union[List[str], int]:
    if ' ' in str:
        return str.split()
    if ',' in str:
        temp_string = str.replace(',', ' ')
        return temp_string.split()
    tally: int = 0
    idx: int = 1
    length: int = len(str)
    while idx <= length:
        ch: str = str[idx - 1]  # zero-based indexing in Python
        if ch.islower():
            ascii_val: int = ord(ch)
            if ascii_val % 2 == 0:
                tally += 1
        idx += 1
    return tally