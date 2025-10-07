from typing import Dict


def encode(inputMessage: str) -> str:
    vowelSet: str = "AEIOUaeiou"
    substitutionMap: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in vowelSet}

    swappedCaseMessage = []
    for symbol in inputMessage:
        if symbol.isupper():
            swappedCaseMessage.append(symbol.lower())
        elif symbol.islower():
            swappedCaseMessage.append(symbol.upper())
        else:
            swappedCaseMessage.append(symbol)

    finalCharacters = [
        substitutionMap[elem] if elem in vowelSet else elem for elem in swappedCaseMessage
    ]

    return "".join(finalCharacters)