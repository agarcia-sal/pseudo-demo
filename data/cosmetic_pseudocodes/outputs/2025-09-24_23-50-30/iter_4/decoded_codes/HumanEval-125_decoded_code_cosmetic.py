from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    elif ',' in text:
        temp = text.replace(',', ' ')
        return temp.split()
    else:
        filtered_chars = [c for c in text if c.islower() and (ord(c) % 2 == 0)]
        return len(filtered_chars)