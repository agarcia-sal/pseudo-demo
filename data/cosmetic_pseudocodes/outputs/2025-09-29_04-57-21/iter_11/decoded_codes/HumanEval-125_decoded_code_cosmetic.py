from typing import Union, List


def split_words(text: str) -> Union[int, List[str]]:
    if ' ' not in text:
        if ',' in text:
            temp_str = text.replace(',', ' ')
            return temp_str.split()
        else:
            tally = 0
            for char in text:
                if 'a' <= char <= 'z' and (ord(char) % 2) == 0:
                    tally += 1
            return tally
    else:
        return text.split()