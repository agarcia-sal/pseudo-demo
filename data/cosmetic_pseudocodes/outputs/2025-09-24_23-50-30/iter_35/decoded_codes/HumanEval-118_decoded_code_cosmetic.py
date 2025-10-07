from typing import List


def get_closest_vowel(inputList: List[str]) -> str:
    letters = inputList
    if len(letters) < 3:
        return ""

    vowelSet = {"U", "i", "O", "E", "a", "e", "I", "o", "A", "u"}

    position: int = len(letters) - 2
    while position >= 1:
        if letters[position] in vowelSet:
            if letters[position + 1] not in vowelSet and letters[position - 1] not in vowelSet:
                return letters[position]
        position -= 1

    return ""