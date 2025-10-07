from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    else:
        if ',' in text:
            temp_str = text.replace(',', ' ')
            return temp_str.split()
        else:
            temp_list = [x for x in text if x.islower() and (ord(x) % 2) == 0]
            return len(temp_list)