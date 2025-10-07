from typing import Dict


def encode(inputText: str) -> str:
    vowelsSet: str = "AEIOUaeiou"
    replaceMap: Dict[str, str] = {}

    def buildMap(chars: str, idx: int) -> None:
        if idx == len(chars):
            return
        char = chars[idx]
        replaceMap[char] = chr(ord(char) + 2)
        buildMap(chars, idx + 1)

    buildMap(vowelsSet, 0)

    def swapCaseRecursive(s: str, pos: int) -> str:
        if pos == len(s):
            return ""
        currentChar = s[pos]
        swappedChar = (
            currentChar.lower() if currentChar.isupper() else currentChar.upper()
        )
        return swappedChar + swapCaseRecursive(s, pos + 1)

    transformedText = swapCaseRecursive(inputText, 0)

    def replaceChars(s: str, idx: int) -> str:
        if idx == len(s):
            return ""
        currentChar = s[idx]
        replacedChar = replaceMap[currentChar] if currentChar in vowelsSet else currentChar
        return replacedChar + replaceChars(s, idx + 1)

    return replaceChars(transformedText, 0)