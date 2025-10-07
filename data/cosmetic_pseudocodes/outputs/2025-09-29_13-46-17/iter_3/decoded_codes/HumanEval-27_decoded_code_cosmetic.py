from typing import List


def flip_case(inputString: str) -> str:
    if inputString == "":
        return ""

    def toggleCaseAtIndex(idx: int, s: str) -> str:
        if idx > len(s):
            return ""
        currentChar = s[idx - 1]
        if "a" <= currentChar <= "z":
            toggledChar = currentChar.upper()
        elif "A" <= currentChar <= "Z":
            toggledChar = currentChar.lower()
        else:
            toggledChar = currentChar
        return toggledChar + toggleCaseAtIndex(idx + 1, s)

    return toggleCaseAtIndex(1, inputString)