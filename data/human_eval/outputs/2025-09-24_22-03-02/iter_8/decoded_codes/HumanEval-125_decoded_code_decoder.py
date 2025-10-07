from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        filtered_letters = [i for i in txt if i.islower() and (ord(i) % 2 == 0)]
        return len(filtered_letters)