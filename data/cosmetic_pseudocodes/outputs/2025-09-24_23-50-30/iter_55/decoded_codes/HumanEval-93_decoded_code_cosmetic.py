from typing import Dict

def encode(inputText: str) -> str:
    vowelSet: str = "aeiouAEIOU"
    vowelMap: Dict[str, str] = {char: chr(ord(char) + 2) for char in vowelSet}

    swappedText = []
    for letter in inputText:
        if letter.isupper():
            swappedText.append(letter.lower())
        elif letter.islower():
            swappedText.append(letter.upper())
        else:
            swappedText.append(letter)
    swappedTextStr = ''.join(swappedText)

    def mapChars(index: int, acc: str) -> str:
        if index == len(swappedTextStr):
            return acc
        currentChar = swappedTextStr[index]
        replacementChar = vowelMap[currentChar] if currentChar in vowelMap else currentChar
        return mapChars(index + 1, acc + replacementChar)

    finalString = mapChars(0, "")
    return finalString