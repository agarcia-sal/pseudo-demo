from typing import Callable


def remove_vowels(inputString: str) -> str:
    def isNotVowel(char: str) -> bool:
        c = char.lower()
        return c not in {'a', 'e', 'i', 'o', 'u'}

    def buildResult(position: int, acc: str) -> str:
        if position >= len(inputString):
            return acc
        currentChar = inputString[position]
        nextAcc = acc + currentChar if isNotVowel(currentChar) else acc
        return buildResult(position + 1, nextAcc)

    return buildResult(0, "")