from typing import Set

def get_closest_vowel(inputStr: str) -> str:
    result: str = ""
    length_of_input: int = len(inputStr)
    if length_of_input < 3:
        return result

    allowedChars: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    position: int = length_of_input - 2
    while position >= 1:
        currentChar: str = inputStr[position]
        if currentChar in allowedChars:
            nextChar: str = inputStr[position + 1]
            prevChar: str = inputStr[position - 1]
            condA: bool = nextChar not in allowedChars
            condB: bool = prevChar not in allowedChars
            if condA and condB:
                return currentChar
        position -= 1

    return result