from typing import Union, List


def split_words(text: str) -> Union[int, List[str]]:
    if not (' ' in text or ',' in text):
        filtered_chars = [ch for ch in text if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]
        return len(filtered_chars)
    if ' ' in text:
        return text.split()
    if ',' in text:
        interim = ''.join(' ' if symbol == ',' else symbol for symbol in text)
        return interim.split()