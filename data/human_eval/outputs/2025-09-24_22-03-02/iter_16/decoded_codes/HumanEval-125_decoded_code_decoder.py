from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_txt = txt.replace(',', ' ')
        return replaced_txt.split()
    else:
        count_list = []
        for i in txt:
            if i.islower() and (ord(i) % 2 == 0):
                count_list.append(i)
        return len(count_list)