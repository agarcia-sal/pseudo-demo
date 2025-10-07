from typing import Dict


def encode(message: str) -> str:
    vowelChars: str = "aeiouAEIOU"
    mapping: Dict[str, str] = {}
    index: int = 0

    while index < len(vowelChars):
        currentChar: str = vowelChars[index]
        mapping[currentChar] = chr(ord(currentChar) + 2)
        index += 1

    swappedMessage: str = ""
    pos: int = 0

    while pos < len(message):
        ch: str = message[pos]
        if ch.isupper():
            swappedMessage += ch.lower()
        elif ch.islower():
            swappedMessage += ch.upper()
        else:
            swappedMessage += ch
        pos += 1

    result: str = ""
    cursor: int = 0

    while cursor < len(swappedMessage):
        character: str = swappedMessage[cursor]
        if character in mapping:
            result += mapping[character]
        else:
            result += character
        cursor += 1

    return result