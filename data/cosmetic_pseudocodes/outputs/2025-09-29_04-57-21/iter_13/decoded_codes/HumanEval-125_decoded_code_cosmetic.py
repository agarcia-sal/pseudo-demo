from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    if ',' not in text:
        filtered_chars = [ch for ch in text if ch.islower() and (ord(ch) % 2) == 0]
        return len(filtered_chars)
    altered_text = ''.join(' ' if ch == ',' else ch for ch in text)
    return altered_text.split()