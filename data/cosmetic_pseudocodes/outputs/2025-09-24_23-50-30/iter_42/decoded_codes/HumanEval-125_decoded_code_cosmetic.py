from typing import List, Union


def split_words(inputValue: str) -> Union[List[str], int]:
    resultList: List[str] = []

    def splitByWhitespace(s: str) -> None:
        index: int = 0
        length: int = len(s)
        while index < length:
            startIndex = index
            while index < length and s[index] != ' ':
                index += 1
            if startIndex < index:
                resultList.append(s[startIndex:index])
            while index < length and s[index] == ' ':
                index += 1

    if any(c == ' ' for c in inputValue):
        splitByWhitespace(inputValue)
        return resultList

    if any(c == ',' for c in inputValue):
        replacementString = ''.join(' ' if c == ',' else c for c in inputValue)
        splitByWhitespace(replacementString)
        return resultList

    counter: int = 0
    for ch in inputValue:
        asciiCode = ord(ch)
        isLower = 'a' <= ch <= 'z'
        isEvenAscii = (asciiCode % 2) == 0
        if isLower and isEvenAscii:
            counter += 1

    return counter