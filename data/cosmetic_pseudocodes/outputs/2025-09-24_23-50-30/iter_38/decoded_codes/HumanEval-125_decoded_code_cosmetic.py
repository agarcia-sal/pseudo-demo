from typing import Union, List


def split_words(input_str: str) -> Union[List[str], int]:
    if ' ' in input_str:
        return input_str.split()
    elif ',' in input_str:
        temp_str = input_str.replace(',', ' ')
        return temp_str.split()
    else:
        filtered_chars = [ch for ch in input_str if ch.islower() and (ord(ch) % 2 == 0)]
        return len(filtered_chars)