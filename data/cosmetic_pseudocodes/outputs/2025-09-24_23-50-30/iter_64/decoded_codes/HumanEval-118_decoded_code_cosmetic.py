from typing import Set


def get_closest_vowel(inputStr: str) -> str:
    vset: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def loop_decreasing(pos: int) -> str:
        if pos < 1:
            return ""
        currChar = inputStr[pos]
        prevChar = inputStr[pos - 1]
        nextChar = inputStr[pos + 1]

        if currChar in vset:
            if prevChar not in vset and nextChar not in vset:
                return currChar
            else:
                return loop_decreasing(pos - 1)
        else:
            return loop_decreasing(pos - 1)

    if len(inputStr) < 3:
        return ""
    return loop_decreasing(len(inputStr) - 2)