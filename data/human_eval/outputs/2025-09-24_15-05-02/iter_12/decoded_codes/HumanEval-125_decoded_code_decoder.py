from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        txt = txt.replace(",", " ")
        return txt.split()
    else:
        count = 0
        for character in txt:
            if character.islower() and (ord(character) % 2 == 0):
                count += 1
        return count