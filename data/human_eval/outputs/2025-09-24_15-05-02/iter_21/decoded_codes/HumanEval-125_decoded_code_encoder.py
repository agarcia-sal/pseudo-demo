from typing import Union, List

def split_words(text: str) -> Union[List[str], int]:
    if " " in text:
        return text.split()
    elif "," in text:
        replaced_text = text.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_list = [ch for ch in text if ch.islower() and (ord(ch) % 2) == 0]
        return len(filtered_list)