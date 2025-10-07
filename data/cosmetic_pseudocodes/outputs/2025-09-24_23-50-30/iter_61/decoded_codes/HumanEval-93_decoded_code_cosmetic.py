from typing import Dict, Set

def encode(inputStr: str) -> str:
    alphabetSet: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    replacementMap: Dict[str, str] = {}
    alphabetList = list(alphabetSet)
    for idx in range(len(alphabetList)):
        currentChar = alphabetList[idx]
        replacementChar = chr(ord(currentChar) + 2)
        replacementMap[currentChar] = replacementChar

    def swapCaseRec(pos: int, acc: str) -> str:
        if pos == len(inputStr):
            return acc
        charAtPos = inputStr[pos]
        if 'a' <= charAtPos <= 'z':
            swappedChar = charAtPos.upper()
        elif 'A' <= charAtPos <= 'Z':
            swappedChar = charAtPos.lower()
        else:
            swappedChar = charAtPos
        return swapCaseRec(pos + 1, acc + swappedChar)

    swapped = swapCaseRec(0, "")

    def replaceVowelsRec(index: int, result: str) -> str:
        if index == len(swapped):
            return result
        character = swapped[index]
        toAppend = replacementMap[character] if character in alphabetSet else character
        return replaceVowelsRec(index + 1, result + toAppend)

    return replaceVowelsRec(0, "")