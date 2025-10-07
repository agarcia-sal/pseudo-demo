from typing import Dict

def encode(inputText: str) -> str:
    vowelsCollection: str = "aeiouAEIOU"
    vowelMap: Dict[str, str] = {}
    index: int = 0
    while index < len(vowelsCollection):
        currentChar: str = vowelsCollection[index]
        charCode: int = ord(currentChar)
        incrementedCode: int = charCode + 2
        mappedChar: str = chr(incrementedCode)
        vowelMap[currentChar] = mappedChar
        index += 1

    alteredText: str = ""
    pos: int = 0
    while pos < len(inputText):
        ch: str = inputText[pos]
        if ch.isupper():
            swappedChar: str = ch.lower()
        elif ch.islower():
            swappedChar = ch.upper()
        else:
            swappedChar = ch
        alteredText += swappedChar
        pos += 1

    finalResult: str = ""
    cursor: int = 0
    while cursor < len(alteredText):
        symbol: str = alteredText[cursor]
        if symbol in vowelMap:
            finalResult += vowelMap[symbol]
        else:
            finalResult += symbol
        cursor += 1

    return finalResult