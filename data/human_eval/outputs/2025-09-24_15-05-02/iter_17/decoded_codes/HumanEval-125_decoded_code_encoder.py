from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(",", " ")
        return replaced_txt.split()
    else:
        filtered_list = [char for char in txt if char.islower() and ord(char) % 2 == 0]
        return len(filtered_list)