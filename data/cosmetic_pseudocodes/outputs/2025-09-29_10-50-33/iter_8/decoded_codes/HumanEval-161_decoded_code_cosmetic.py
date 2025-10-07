from typing import List


def solve(sourceText: str) -> None:
    def toggleCaseAt(position: int, textArray: List[str]) -> None:
        c = textArray[position]
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            return
        if 'a' <= c <= 'z':
            textArray[position] = c.upper()
        else:
            textArray[position] = c.lower()

    FLAG_SWITCH = False
    charsList = list(sourceText)

    def processAtPosition(pos: int) -> None:
        nonlocal FLAG_SWITCH
        if pos >= len(charsList):
            return

        c = charsList[pos]
        isAlpha = ('a' <= c <= 'z') or ('A' <= c <= 'Z')
        if isAlpha:
            toggleCaseAt(pos, charsList)
            FLAG_SWITCH = True

        processAtPosition(pos + 1)

    processAtPosition(0)

    reconstructedText = ''.join(charsList)

    if not FLAG_SWITCH:
        print(reconstructedText[::-1])
    else:
        print(reconstructedText)