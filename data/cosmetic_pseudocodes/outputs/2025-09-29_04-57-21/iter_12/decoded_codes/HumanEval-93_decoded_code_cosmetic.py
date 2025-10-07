from typing import Dict


def encode(message: str) -> str:
    vowelChars: str = "aeiouAEIOU"
    shiftedVowels: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelChars):
        originalChar: str = vowelChars[idx]
        incrementedChar: str = chr(ord(originalChar) + 2)
        shiftedVowels[originalChar] = incrementedChar
        idx += 1

    swappedMessage: str = ""
    position: int = 0
    while position < len(message):
        currentChar: str = message[position]
        if 'A' <= currentChar <= 'Z':
            swappedMessage += currentChar.lower()
        elif 'a' <= currentChar <= 'z':
            swappedMessage += currentChar.upper()
        else:
            swappedMessage += currentChar
        position += 1

    output: str = ""
    characterIterator: int = 0
    while characterIterator < len(swappedMessage):
        charAtPos: str = swappedMessage[characterIterator]
        if charAtPos in shiftedVowels:
            output += shiftedVowels[charAtPos]
        else:
            output += charAtPos
        characterIterator += 1

    return output