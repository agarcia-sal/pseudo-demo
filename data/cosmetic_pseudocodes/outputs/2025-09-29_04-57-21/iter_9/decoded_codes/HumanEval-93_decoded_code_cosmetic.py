from typing import Dict

def encode(message: str) -> str:
    swapVowels: str = "aeiouAEIOU"
    shiftedChars: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in swapVowels}

    transformedMessage: str = ""
    for char in message:
        if char.isupper():
            transformedMessage += char.lower()
        elif char.islower():
            transformedMessage += char.upper()
        else:
            transformedMessage += char

    outputString: str = ""
    iterator: int = 0
    length: int = len(transformedMessage)
    while iterator < length:
        currentChar = transformedMessage[iterator]
        if currentChar in swapVowels:
            outputString += shiftedChars[currentChar]
        else:
            outputString += currentChar
        iterator += 1

    return outputString