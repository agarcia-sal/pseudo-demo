from typing import Union, List

def split_words(txt: str) -> Union[List[str], int]:
    if " " in txt:
        return txt.split()
    elif "," in txt:
        replaced_text = txt.replace(",", " ")
        return replaced_text.split()
    else:
        count_list = []
        index = 0
        while index < len(txt):
            i = txt[index]
            if i.islower() and (ord(i) % 2 == 0):
                count_list.append(i)
            index += 1
        return len(count_list)