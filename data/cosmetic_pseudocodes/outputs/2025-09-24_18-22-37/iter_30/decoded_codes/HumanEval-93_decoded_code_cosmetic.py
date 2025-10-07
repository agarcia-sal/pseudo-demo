from typing import Dict


def encode(textInput: str) -> str:
    vowelSet: str = "aeiouAEIOU"
    vowelMap: Dict[str, str] = {}
    counter: int = 0
    while counter < len(vowelSet):
        charAtPos: str = vowelSet[counter]
        nextChar: str = chr(ord(charAtPos) + 2)
        vowelMap[charAtPos] = nextChar
        counter += 1

    swappedText: str = ""
    idx: int = 0
    while idx < len(textInput):
        currentChar: str = textInput[idx]
        if "a" <= currentChar <= "z":
            swappedText += currentChar.upper()
        elif "A" <= currentChar <= "Z":
            swappedText += currentChar.lower()
        else:
            swappedText += currentChar
        idx += 1

    resultString: str = ""
    pos: int = 0
    while pos < len(swappedText):
        letter: str = swappedText[pos]
        if letter in vowelMap:
            resultString += vowelMap[letter]
        else:
            resultString += letter
        pos += 1

    return resultString