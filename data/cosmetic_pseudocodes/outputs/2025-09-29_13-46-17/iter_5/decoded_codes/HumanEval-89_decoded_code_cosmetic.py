from typing import Callable

def encrypt(input_string: str) -> str:
    alphaSet: str = "abcdefghijklmnopqrstuvwxyz"
    lenAlpha: int = 26

    def helper(pos: int, acc: str) -> str:
        if pos >= len(input_string):
            return acc
        ch: str = input_string[pos]
        foundIndex: int = -1
        for idx in range(lenAlpha):
            if alphaSet[idx] == ch:
                foundIndex = idx
                break
        if foundIndex < 0:
            nextAcc: str = acc + ch
        else:
            indexShifted: int = (foundIndex + 4) % lenAlpha
            nextAcc = acc + alphaSet[indexShifted]
        return helper(pos + 1, nextAcc)

    return helper(0, "")