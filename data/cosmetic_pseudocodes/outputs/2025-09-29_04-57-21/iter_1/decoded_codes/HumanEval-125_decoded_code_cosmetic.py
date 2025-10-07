from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        altered_text = text.replace(",", " ")
        return altered_text.split()
    else:
        total = sum(1 for ch in text if ch.islower() and (ord(ch) % 2) == 0)
        return total