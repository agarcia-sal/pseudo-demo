from typing import Dict

def encode(inputText: str) -> str:
    vowelSet = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    substituteMap: Dict[str, str] = {}
    for element in vowelSet:
        substituteMap[element] = chr(ord(element) + 2)

    flippedText = []
    for char in inputText:
        if 'a' <= char <= 'z':
            # Flip case: convert lowercase to uppercase by reflecting around midpoint
            flippedChar = chr(ord(char) - (ord(char) - ord(char.upper())) * 2)
            flippedText.append(flippedChar)
        elif 'A' <= char <= 'Z':
            # Flip case: convert uppercase to lowercase by reflecting around midpoint
            flippedChar = chr(ord(char) + (ord(char.lower()) - ord(char)) * 2)
            flippedText.append(flippedChar)
        else:
            flippedText.append(char)
    flippedTextStr = "".join(flippedText)

    outputText = []
    idx = 0
    length = len(flippedTextStr)
    while idx < length:
        currentChar = flippedTextStr[idx]
        outputChar = substituteMap[currentChar] if currentChar in vowelSet else currentChar
        outputText.append(outputChar)
        idx += 1

    return "".join(outputText)