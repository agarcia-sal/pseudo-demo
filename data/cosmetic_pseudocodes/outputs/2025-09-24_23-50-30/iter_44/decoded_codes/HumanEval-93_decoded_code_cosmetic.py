from typing import Dict, List

def encode(inputString: str) -> str:
    referenceVowels: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    mappingDict: Dict[str, str] = {item: chr(ord(item) + 2) for item in referenceVowels}
    toggledString: str = ''.join(
        ch.upper() if ch.islower() else ch.lower()
        for ch in inputString
    )
    resultBuilder: List[str] = []

    def processCharacters(index: int) -> None:
        if index >= len(toggledString):
            return
        currentChar: str = toggledString[index]
        replacementChar: str = mappingDict[currentChar] if currentChar in referenceVowels else currentChar
        resultBuilder.append(replacementChar)
        processCharacters(index + 1)

    processCharacters(0)
    return ''.join(resultBuilder)