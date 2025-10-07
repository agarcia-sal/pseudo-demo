from typing import Dict


def encode(inputText: str) -> str:
    alphaSet: str = "AEIOUaeiou"
    shiftMap: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in alphaSet}

    toggledText = []
    for currentChar in inputText:
        if currentChar.isupper():
            toggledText.append(currentChar.lower())
        elif currentChar.islower():
            toggledText.append(currentChar.upper())
        else:
            toggledText.append(currentChar)
    toggledText_str = ''.join(toggledText)

    resultText = ''.join(shiftMap.get(ch, ch) for ch in toggledText_str)
    return resultText