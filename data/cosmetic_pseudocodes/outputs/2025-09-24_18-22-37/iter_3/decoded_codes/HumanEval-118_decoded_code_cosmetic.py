from typing import Set

def get_closest_vowel(word: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    length: int = len(word)
    if length < 3:
        return ""

    pos: int = length - 2
    while pos >= 1:
        c: str = word[pos]
        if c in vowels:
            left_char: str = word[pos - 1]
            right_char: str = word[pos + 1]
            if not (left_char in vowels or right_char in vowels):
                return c
        pos -= 1

    return ""