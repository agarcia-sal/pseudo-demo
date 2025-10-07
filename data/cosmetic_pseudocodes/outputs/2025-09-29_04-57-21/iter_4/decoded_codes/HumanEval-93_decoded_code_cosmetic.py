from typing import Dict

def encode(message: str) -> str:
    vowelChars: str = "AEIOUaeiou"
    vowelShiftMap: Dict[str, str] = {}
    for character in vowelChars:
        shiftedCharAscii: int = ord(character) + 2
        vowelShiftMap[character] = chr(shiftedCharAscii)
    toggledMessage: str = ""
    for symbol in message:
        if symbol.isupper():
            toggledMessage += symbol.lower()
        elif symbol.islower():
            toggledMessage += symbol.upper()
        else:
            toggledMessage += symbol
    encodedMessage: str = ""
    index: int = 0
    while index < len(toggledMessage):
        currentChar: str = toggledMessage[index]
        if currentChar in vowelShiftMap:
            encodedMessage += vowelShiftMap[currentChar]
        else:
            encodedMessage += currentChar
        index += 1
    return encodedMessage