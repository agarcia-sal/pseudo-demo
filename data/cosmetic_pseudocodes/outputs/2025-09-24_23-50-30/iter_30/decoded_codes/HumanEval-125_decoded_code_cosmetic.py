from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    if "," in input_string:
        temp_string = input_string.replace(",", " ")
        return temp_string.split()
    filtered_chars = [ch for ch in input_string if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]
    return len(filtered_chars)