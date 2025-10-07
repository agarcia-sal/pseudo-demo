from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    if " " not in text:
        if "," in text:
            interim_string: str = text.replace(",", " ")
            return interim_string.split()
        tally: int = 0
        char_list: List[str] = list(text)
        idx: int = 0
        while idx < len(char_list):
            current_char: str = char_list[idx]
            if current_char.islower() and (ord(current_char) % 2 == 0):
                tally += 1
            idx += 1
        return tally
    return text.split()