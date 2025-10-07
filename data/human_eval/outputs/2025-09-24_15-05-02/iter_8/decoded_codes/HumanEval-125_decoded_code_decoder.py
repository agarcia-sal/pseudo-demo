from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(",", " ").split()
    else:
        count: int = 0
        for character in txt:
            if character.islower() and (ord(character) % 2 == 0):
                count += 1
        return count