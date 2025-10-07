from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    if ' ' in text:
        return text.split()
    elif ',' in text:
        temp_string = ''.join(' ' if ch == ',' else ch for ch in text)
        return temp_string.split()
    else:
        tally = 0
        for ch in text:
            ascii_val = ord(ch)
            if ch.islower() and (ascii_val % 2) == 0:
                tally += 1
        return tally