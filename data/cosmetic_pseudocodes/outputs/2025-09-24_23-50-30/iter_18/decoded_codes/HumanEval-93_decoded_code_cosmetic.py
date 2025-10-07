from typing import List, Dict

def encode(message: str) -> str:
    swapCaseChars: List[str] = []
    for position in range(len(message)):
        currentChar = message[position]
        if currentChar.isupper():
            swapCaseChars.append(currentChar.lower())
        else:
            swapCaseChars.append(currentChar.upper())

    vowelsDict: Dict[str, str] = {}
    for char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        asciiVal = ord(char)
        vowelsDict[char] = chr(asciiVal + 2)

    resultBuilder: List[str] = []
    indexCounter = 0
    while indexCounter < len(swapCaseChars):
        ch = swapCaseChars[indexCounter]
        if ch in vowelsDict:
            resultBuilder.append(vowelsDict[ch])
        else:
            resultBuilder.append(ch)
        indexCounter += 1

    return ''.join(resultBuilder)