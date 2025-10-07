from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' not in text:
        if ',' in text:
            replaced_string = text.replace(',', ' ')
            return replaced_string.split()
        else:
            filtered_chars = [ch for ch in text if ch.lower() and (ord(ch) % 2 == 0)]
            total = len(filtered_chars)
            return total
    else:
        return text.split()