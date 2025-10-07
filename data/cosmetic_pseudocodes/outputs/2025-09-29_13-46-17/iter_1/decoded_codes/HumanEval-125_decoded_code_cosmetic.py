from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        words = text.split()
        return words
    elif "," in text:
        new_text = text.replace(",", " ")
        words = new_text.split()
        return words
    else:
        letters = [ch for ch in text if ch.islower() and (ord(ch) % 2 == 0)]
        total = len(letters)
        return total