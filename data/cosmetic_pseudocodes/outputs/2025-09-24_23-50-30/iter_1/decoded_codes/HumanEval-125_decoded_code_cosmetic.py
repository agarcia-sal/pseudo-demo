from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    else:
        if ',' in text:
            temp_string = text.replace(',', ' ')
            return temp_string.split()
        else:
            filtered_chars = [ch for ch in text if ch.islower() and (ord(ch) % 2) == 0]
            count = len(filtered_chars)
            return count