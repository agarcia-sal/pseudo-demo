from typing import Dict


def encode(inputText: str) -> str:
    vowelsList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowelMap: Dict[str, str] = {}
    index = 0
    while index < len(vowelsList):
        currentChar = vowelsList[index]
        vowelMap[currentChar] = chr(ord(currentChar) + 2)
        index += 1

    alteredText = ""
    position = 0
    while position < len(inputText):
        origChar = inputText[position]
        if origChar.isupper():
            convertedChar = origChar.lower()
        else:
            convertedChar = origChar.upper()
        alteredText += convertedChar
        position += 1

    outputText = ""
    for character in alteredText:
        if character in vowelsList:
            outputText += vowelMap[character]
        else:
            outputText += character

    return outputText