from typing import Dict

def encode(inputText: str) -> str:
    vowelsSet: str = "aeiouAEIOU"
    replacementMap: Dict[str, str] = {}
    for originalCh in vowelsSet:
        replacementMap[originalCh] = chr(ord(originalCh) + 2)

    swappedText: str = ""
    for ch in inputText:
        if 'a' <= ch <= 'z':
            swappedText += ch.upper()
        elif 'A' <= ch <= 'Z':
            swappedText += ch.lower()
        else:
            swappedText += ch

    result: str = ""
    for currentChar in swappedText:
        if currentChar in vowelsSet:
            result += replacementMap[currentChar]
        else:
            result += currentChar

    return result