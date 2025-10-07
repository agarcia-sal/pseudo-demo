from typing import Dict

def encode(inputText: str) -> str:
    swapVowels: str = "AEIOUaeiou"
    translationMap: Dict[str, str] = {}
    for char in swapVowels:
        asciiNum: int = ord(char)
        incrementedAscii: int = asciiNum + 2
        mappedChar: str = chr(incrementedAscii)
        translationMap[char] = mappedChar

    toggledText_chars = []
    for currentChar in inputText:
        if currentChar.isupper():
            toggledChar = currentChar.lower()
        elif currentChar.islower():
            toggledChar = currentChar.upper()
        else:
            toggledChar = currentChar
        toggledText_chars.append(toggledChar)
    toggledText = "".join(toggledText_chars)

    output_chars = []
    for symbol in toggledText:
        if symbol in translationMap:
            replacement = translationMap[symbol]
            output_chars.append(replacement)
        else:
            output_chars.append(symbol)
    outputString = "".join(output_chars)

    return outputString