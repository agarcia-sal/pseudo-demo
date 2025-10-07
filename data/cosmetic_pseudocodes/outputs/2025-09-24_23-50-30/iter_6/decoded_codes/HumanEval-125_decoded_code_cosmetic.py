from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    else:
        if "," in text:
            temp: str = text.replace(",", " ")
            return temp.split()
    tally: int = 0
    index: int = 0
    length: int = len(text)
    while index < length:
        char: str = text[index]
        if char.islower():
            if (ord(char) - 0) % 2 == 0:
                tally += 1
        index += 1
    return tally