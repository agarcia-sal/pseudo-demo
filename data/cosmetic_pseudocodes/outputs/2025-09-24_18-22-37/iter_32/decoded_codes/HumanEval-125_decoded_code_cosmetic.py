from typing import Union, List


def split_words(text: str) -> Union[List[str], int]:
    flag1: bool = False
    flag2: bool = False

    idx: int = 0
    while idx < len(text) and not flag1:
        if text[idx] == ' ':
            flag1 = True
        idx += 1

    if flag1:
        return text.split()
    else:
        idx = 0
        while idx < len(text) and not flag2:
            if text[idx] == ',':
                flag2 = True
            idx += 1

        if flag2:
            tempText: str = ""
            totalChars: int = len(text)
            idx = 0
            while idx < totalChars:
                if text[idx] == ',':
                    tempText += ' '
                else:
                    tempText += text[idx]
                idx += 1
            return tempText.split()
        else:
            chars: List[str] = []
            for idx in range(len(text)):
                ch: str = text[idx]
                asciiVal: int = ord(ch)
                if 'a' <= ch <= 'z':
                    modResult: int = asciiVal % 2
                    if modResult == 0:
                        chars.append(ch)
            tally: int = len(chars)
            return tally