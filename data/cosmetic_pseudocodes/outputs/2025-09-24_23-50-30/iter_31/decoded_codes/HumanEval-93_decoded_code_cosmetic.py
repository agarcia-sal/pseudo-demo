from typing import Dict, List


def encode(inputText: str) -> str:
    alphabet: str = "AEIOUaeiou"
    shiftedMap: Dict[str, str] = {}
    for symbol in alphabet:
        ascVal = ord(symbol)
        mappedChar = chr(ascVal + 2)
        shiftedMap[symbol] = mappedChar

    swappedText: List[str] = []
    for unit in inputText:
        if unit.isupper():
            swappedText.append(unit.lower())
        elif unit.islower():
            swappedText.append(unit.upper())
        else:
            swappedText.append(unit)

    transformedText: List[str] = []
    for element in swappedText:
        outputChar = shiftedMap[element] if element in alphabet else element
        transformedText.append(outputChar)

    return "".join(transformedText)