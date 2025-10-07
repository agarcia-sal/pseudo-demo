from typing import Union, List


def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        temp = txt.replace(",", " ")
        return temp.split()
    else:
        count = sum(1 for c in txt if c.islower() and (ord(c) % 2) == 0)
        return count