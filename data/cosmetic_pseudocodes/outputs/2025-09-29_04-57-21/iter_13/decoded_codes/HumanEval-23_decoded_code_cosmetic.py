from typing import Callable

def strlen(string: str) -> int:
    characterCount: int = 0

    def countCharacters(index: int) -> int:
        nonlocal characterCount
        if index == len(string):
            return characterCount
        characterCount += 1
        return countCharacters(index + 1)

    return countCharacters(0)