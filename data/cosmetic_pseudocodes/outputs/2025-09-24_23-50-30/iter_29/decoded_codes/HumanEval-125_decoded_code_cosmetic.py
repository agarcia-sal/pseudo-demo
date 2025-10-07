from typing import Union, List


def split_words(inputStr: str) -> Union[List[str], int]:
    if ' ' in inputStr:
        return inputStr.split()
    elif ',' in inputStr:
        tempStr = inputStr.replace(',', ' ')
        return tempStr.split()
    else:
        filtered_chars = [ch for ch in inputStr if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]
        return len(filtered_chars)