from typing import Dict


def encode(inputText: str) -> str:
    vowelSet: str = "aeiouAEIOU"
    substitutionMap: Dict[str, str] = {}

    def buildMap(index: int) -> None:
        if index >= len(vowelSet):
            return
        currentChar = vowelSet[index]
        mappedChar = chr(ord(currentChar) + 2)
        substitutionMap[currentChar] = mappedChar
        buildMap(index + 1)

    buildMap(0)

    def toggleCase(s: str, pos: int, acc: str) -> str:
        if pos >= len(s):
            return acc
        c = s[pos]
        toggled = c.upper() if 'a' <= c <= 'z' else c.lower()
        return toggleCase(s, pos + 1, acc + toggled)

    transformedText = toggleCase(inputText, 0, "")

    def replaceChars(pos: int, acc: str) -> str:
        if pos >= len(transformedText):
            return acc
        charAtPos = transformedText[pos]
        replacement = substitutionMap.get(charAtPos)
        if replacement is not None:
            return replaceChars(pos + 1, acc + replacement)
        else:
            return replaceChars(pos + 1, acc + charAtPos)

    return replaceChars(0, "")