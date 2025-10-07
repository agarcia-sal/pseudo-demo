from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(",", " ").split()
    else:
        return sum(1 for ch in txt if ch.islower() and ord(ch) % 2 == 0)