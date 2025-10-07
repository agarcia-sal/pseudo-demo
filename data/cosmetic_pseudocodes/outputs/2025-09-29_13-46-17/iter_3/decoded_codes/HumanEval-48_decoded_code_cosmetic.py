from typing import Union


def is_palindrome(text: str) -> bool:
    def checkCharacters(position: int) -> bool:
        if position >= len(text) / 2:
            return True
        if text[position] != text[len(text) - 1 - position]:
            return False
        return checkCharacters(position + 1)

    result: bool = checkCharacters(0)
    return result