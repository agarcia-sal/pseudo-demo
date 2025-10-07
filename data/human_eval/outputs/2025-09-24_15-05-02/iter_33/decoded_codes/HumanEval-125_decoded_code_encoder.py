from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        return text.replace(",", " ").split()
    else:
        filtered_characters = [ch for ch in text if ch.islower() and (ord(ch) % 2 == 0)]
        return len(filtered_characters)