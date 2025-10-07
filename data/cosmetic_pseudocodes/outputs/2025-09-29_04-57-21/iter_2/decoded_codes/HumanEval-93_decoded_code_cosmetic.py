from typing import Dict

def encode(message: str) -> str:
    alternates: str = "aeiouAEIOU"
    mapping: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in alternates}

    swappedMessage: str = ""
    for char in message:
        code: int = ord(char)
        if 65 <= code <= 90:
            swappedMessage += chr(code + 32)  # Upper to lower
        elif 97 <= code <= 122:
            swappedMessage += chr(code - 32)  # Lower to upper
        else:
            swappedMessage += char

    result: str = ""
    for element in swappedMessage:
        if element in mapping:
            result += mapping[element]
        else:
            result += element

    return result