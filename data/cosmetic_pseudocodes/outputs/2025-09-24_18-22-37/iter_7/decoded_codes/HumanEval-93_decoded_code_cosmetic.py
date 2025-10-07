from typing import Dict


def encode(inputText: str) -> str:
    vowelCharacters: str = "aeiouAEIOU"
    mappingDict: Dict[str, str] = {}
    indexVar: int = 0
    while indexVar < len(vowelCharacters):
        currentChar: str = vowelCharacters[indexVar]
        asciiVal: int = ord(currentChar)
        shiftedCharCode: int = asciiVal + 2
        mappedChar: str = chr(shiftedCharCode)
        mappingDict[currentChar] = mappedChar
        indexVar += 1

    swappedText: str = ""
    pos: int = 0
    while pos < len(inputText):
        charInText: str = inputText[pos]
        if ('a' <= charInText <= 'z') or ('A' <= charInText <= 'Z'):
            if charInText.islower():
                upperChar: str = charInText.upper()
                swappedText += upperChar
            else:
                lowerChar: str = charInText.lower()
                swappedText += lowerChar
        else:
            swappedText += charInText
        pos += 1

    outputString: str = ""
    counter: int = 0
    while counter < len(swappedText):
        currentChar = swappedText[counter]
        if currentChar in mappingDict:
            mappedChar = mappingDict[currentChar]
            outputString += mappedChar
        else:
            outputString += currentChar
        counter += 1

    return outputString