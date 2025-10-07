from typing import Union, List


def split_words(inputString: str) -> Union[int, List[str]]:
    if ' ' not in inputString:
        if ',' in inputString:
            tempStr = inputString.replace(',', ' ')
            return tempStr.split()
        else:
            filteredChars = [c for c in inputString if c.islower() and (ord(c) % 2 == 0)]
            return len(filteredChars)
    else:
        return inputString.split()