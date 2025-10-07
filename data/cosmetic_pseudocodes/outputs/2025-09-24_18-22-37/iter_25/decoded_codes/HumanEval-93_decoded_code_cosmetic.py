from typing import Dict

def encode(inputText: str) -> str:
    alteredVowels: str = "AEIOUaeiou"
    mappingTable: Dict[str, str] = {}
    cursor: int = 0

    while cursor < len(alteredVowels):
        currentLetter: str = alteredVowels[cursor]
        asciiNumber: int = ord(currentLetter)
        mappedAscii: int = asciiNumber + 2
        mappedCharacter: str = chr(mappedAscii)
        mappingTable[currentLetter] = mappedCharacter
        cursor += 1

    flippedText: str = ""
    pos: int = 0
    # flip case of every alphabetic char
    while pos < len(inputText):
        currentChar: str = inputText[pos]
        if "A" <= currentChar <= "Z":
            flippedText += chr(ord(currentChar) + (ord("a") - ord("A")))
        elif "a" <= currentChar <= "z":
            flippedText += chr(ord(currentChar) - (ord("a") - ord("A")))
        else:
            flippedText += currentChar
        pos += 1

    resultString: str = ""
    indexVar: int = 0
    while indexVar < len(flippedText):
        characterC: str = flippedText[indexVar]
        if characterC in mappingTable:
            resultString += mappingTable[characterC]
        else:
            resultString += characterC
        indexVar += 1

    return resultString