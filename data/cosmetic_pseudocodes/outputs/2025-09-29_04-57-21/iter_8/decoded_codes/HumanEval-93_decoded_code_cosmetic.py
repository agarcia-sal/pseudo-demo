from typing import Dict


def encode(text: str) -> str:
    lettersToSwitch: str = "aeiouAEIOU"
    mappings: Dict[str, str] = {}
    idx: int = 0
    while idx < len(lettersToSwitch):
        ch: str = lettersToSwitch[idx]
        mappings[ch] = chr(ord(ch) + 2)
        idx += 1

    changedText: str = ""
    pos: int = 0
    while pos < len(text):
        currentChar: str = text[pos]
        if currentChar.islower():
            toggledChar = currentChar.upper()
        elif currentChar.isupper():
            toggledChar = currentChar.lower()
        else:
            toggledChar = currentChar
        changedText += toggledChar
        pos += 1

    result: str = ""
    pointer: int = 0
    while pointer < len(changedText):
        item: str = changedText[pointer]
        if item in mappings:
            result += mappings[item]
        else:
            result += item
        pointer += 1

    return result