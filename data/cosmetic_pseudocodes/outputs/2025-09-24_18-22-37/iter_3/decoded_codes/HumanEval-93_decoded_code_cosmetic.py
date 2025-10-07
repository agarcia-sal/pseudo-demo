from typing import Dict


def encode(inputMessage: str) -> str:
    vowelSet: str = "aeiouAEIOU"
    translationMap: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in vowelSet}

    def toggleCase(s: str) -> str:
        if not s:
            return ""
        firstChar, restStr = s[0], s[1:]
        if firstChar.isupper():
            return firstChar.lower() + toggleCase(restStr)
        elif firstChar.islower():
            return firstChar.upper() + toggleCase(restStr)
        else:
            return firstChar + toggleCase(restStr)

    swappedMessage: str = toggleCase(inputMessage)

    def translateCharacters(index: int, originalStr: str, map_: Dict[str, str]) -> str:
        if index >= len(originalStr):
            return ""
        currentCharacter = originalStr[index]
        replacementCharacter = map_.get(currentCharacter, currentCharacter)
        return replacementCharacter + translateCharacters(index + 1, originalStr, map_)

    return translateCharacters(0, swappedMessage, translationMap)