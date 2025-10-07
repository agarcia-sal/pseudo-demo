from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    elif ',' in text:
        modified_text = text.replace(',', ' ')
        return modified_text.split()
    else:
        count = sum(1 for ch in text if ch.islower() and (ord(ch) % 2 == 0))
        return count