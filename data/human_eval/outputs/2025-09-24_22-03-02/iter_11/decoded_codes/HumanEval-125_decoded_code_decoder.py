from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(",", " ").split()
    else:
        return sum(1 for i in txt if i.islower() and ord(i) % 2 == 0)