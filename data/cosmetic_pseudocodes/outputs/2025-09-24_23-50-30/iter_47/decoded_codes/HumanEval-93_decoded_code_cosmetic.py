from typing import Dict

def encode(theInput: str) -> str:
    letterMap: Dict[str, str] = {}
    vowelsSet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for currentChar in vowelsSet:
        letterMap[currentChar] = chr(ord(currentChar) + 2)

    swappedCase = []
    for currentChar in theInput:
        if 'a' <= currentChar <= 'z':
            swappedCase.append(chr(ord(currentChar) - 32))
        elif 'A' <= currentChar <= 'Z':
            swappedCase.append(chr(ord(currentChar) + 32))
        else:
            swappedCase.append(currentChar)
    swappedCaseStr = ''.join(swappedCase)

    outputChars = []
    for letter in swappedCaseStr:
        if letter not in vowelsSet:
            outputChars.append(letter)
        else:
            outputChars.append(letterMap[letter])

    return ''.join(outputChars)