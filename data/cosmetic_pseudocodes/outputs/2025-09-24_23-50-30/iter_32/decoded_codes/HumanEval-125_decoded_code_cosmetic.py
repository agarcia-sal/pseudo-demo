from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    for char in text:
        if char == ' ':
            return text.split()
    for c in text:
        if c == ',':
            temp_text = [' ' if ch == ',' else ch for ch in text]
            return ''.join(temp_text).split()
    acc = 0
    text_array = list(text)
    idx = 0
    while idx < len(text_array):
        ch = text_array[idx]
        if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0:
            acc += 1
        idx += 1
    return acc