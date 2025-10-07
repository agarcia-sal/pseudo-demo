from typing import Union, List

def split_words(text: str) -> Union[int, List[str]]:
    if ' ' in text:
        return text.split()
    else:
        if ',' in text:
            interim_string = ''.join(' ' if char == ',' else char for char in text)
            return interim_string.split()
        else:
            total = 0
            for letter in text:
                if letter.islower() and (ord(letter) & 1) == 0:
                    total += 1
            return total