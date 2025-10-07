from typing import Dict


def encode(alpha: str) -> str:
    fifthCharCodes: str = "aeiouAEIOU"
    sixthNextChars = ''.join(chr(ord(c) + 2) for c in fifthCharCodes)
    shiftedCharMap: Dict[str, str] = dict(zip(fifthCharCodes, sixthNextChars))

    def swapCaseRecursively(pos: int, acc: str) -> str:
        if pos == len(alpha):
            return acc
        currentChar = alpha[pos]
        if 'A' <= currentChar <= 'Z':
            toggledChar = currentChar.lower()
        else:
            toggledChar = currentChar.upper()
        return swapCaseRecursively(pos + 1, acc + toggledChar)

    toggledMsg = swapCaseRecursively(0, "")

    def substituteRecursively(idx: int, resultAcc: str) -> str:
        if idx == len(toggledMsg):
            return resultAcc
        currentChar = toggledMsg[idx]
        substitutedChar = shiftedCharMap.get(currentChar, currentChar)
        return substituteRecursively(idx + 1, resultAcc + substitutedChar)

    return substituteRecursively(0, "")