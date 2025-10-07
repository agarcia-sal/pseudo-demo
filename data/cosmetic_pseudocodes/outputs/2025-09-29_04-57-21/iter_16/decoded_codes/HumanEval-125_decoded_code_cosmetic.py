from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    else:
        if ',' in text:
            interim_string = text.replace(',', ' ')
            return interim_string.split()
        filtered_chars = [ch for ch in text if ch.islower() and (ord(ch) % 2) == 0]
        return len(filtered_chars)