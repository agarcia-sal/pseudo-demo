from typing import Dict, List

def encode(message: str) -> str:
    def swapCaseCharacters(INPUT: str) -> str:
        # Swap case manually without using str.swapcase()
        return ''.join(
            chr(ord(ch) - 32) if 'a' <= ch <= 'z'
            else chr(ord(ch) + 32) if 'A' <= ch <= 'Z'
            else ch
            for ch in INPUT
        )

    vowelCharacters: List[str] = ['a','e','i','o','u','A','E','I','O','U']
    shiftedVowels: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelCharacters):
        currChar = vowelCharacters[idx]
        shiftedChar = chr(ord(currChar) + 2)
        shiftedVowels[currChar] = shiftedChar
        idx += 1

    transformedMessage: str = swapCaseCharacters(message)

    idx = 0
    resultCharacters: List[str] = []
    while idx < len(transformedMessage):
        currentChar = transformedMessage[idx]
        if currentChar in vowelCharacters:
            resultCharacters.append(shiftedVowels[currentChar])
        else:
            resultCharacters.append(currentChar)
        idx += 1

    return ''.join(resultCharacters)