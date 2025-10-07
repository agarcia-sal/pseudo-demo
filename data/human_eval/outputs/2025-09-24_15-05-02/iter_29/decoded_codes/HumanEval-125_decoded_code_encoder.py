from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        return text.replace(",", " ").split()
    else:
        count = sum(1 for c in text if c.islower() and (ord(c) % 2 == 0))
        return count