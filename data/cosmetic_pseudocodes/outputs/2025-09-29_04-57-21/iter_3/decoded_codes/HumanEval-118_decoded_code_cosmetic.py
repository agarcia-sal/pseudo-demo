from typing import Callable

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowel_set = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

    def checkPosition(pos: int) -> str:
        if pos < 1:
            return ""
        current_char = word[pos]
        if current_char in vowel_set:
            before_char = word[pos - 1]
            after_char = word[pos + 1]
            if before_char not in vowel_set and after_char not in vowel_set:
                return current_char
        return checkPosition(pos - 1)

    return checkPosition(len(word) - 2)