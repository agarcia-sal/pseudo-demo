from typing import Dict


def encode(message: str) -> str:
    letterSwap: str = "aeiouAEIOU"
    shiftedChars: Dict[str, str] = {char: chr(ord(char) + 2) for char in letterSwap}

    invertedMessage: str = ""
    for ch in message:
        if ch.isupper():
            invertedMessage += ch.lower()
        elif ch.islower():
            invertedMessage += ch.upper()
        else:
            invertedMessage += ch

    result: str = ""
    for currentChar in invertedMessage:
        if currentChar in letterSwap:
            result += shiftedChars[currentChar]
        else:
            result += currentChar

    return result