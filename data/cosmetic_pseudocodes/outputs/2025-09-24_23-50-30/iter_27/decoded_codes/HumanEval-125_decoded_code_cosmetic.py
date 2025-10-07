from typing import Union, List

def split_words(inputString: str) -> Union[int, List[str]]:
    if ' ' in inputString:
        return inputString.split()
    if ',' in inputString:
        alteredString = inputString.replace(',', ' ')
        return alteredString.split()
    accumulation = 0
    for i in range(len(inputString)):
        currentChar = inputString[i]
        if currentChar.islower() and (ord(currentChar) % 2 == 0):
            accumulation += 1
    return accumulation