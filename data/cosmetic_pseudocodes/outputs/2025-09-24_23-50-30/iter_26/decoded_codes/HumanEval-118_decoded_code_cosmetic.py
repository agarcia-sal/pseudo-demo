from typing import Set

def get_closest_vowel(inputstring: str) -> str:
    if len(inputstring) < 3:
        return ""

    setX: Set[str] = {"E", "a", "i", "o", "U", "A", "O", "u", "I", "e"}

    def descend_loop(counter: int) -> str:
        if counter < 1:
            return ""
        if (inputstring[counter] in setX and
            not (inputstring[counter + 1] in setX or inputstring[counter - 1] in setX)):
            return inputstring[counter]
        return descend_loop(counter - 1)

    return descend_loop(len(inputstring) - 2)