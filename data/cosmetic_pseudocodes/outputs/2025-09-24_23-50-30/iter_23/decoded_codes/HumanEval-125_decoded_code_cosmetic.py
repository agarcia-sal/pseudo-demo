from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ',' not in text and ' ' in text:
        return text.split()
    if ',' in text:
        temp_text = text.replace(',', ' ')
        return temp_text.split()
    collector: List[str] = [ch for ch in text if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]
    return len(collector)