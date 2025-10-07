from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    allowed_vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    pos_cursor: int = len(word) - 2
    while pos_cursor > 0:
        curr_char: str = word[pos_cursor]
        if curr_char in allowed_vowels:
            if (word[pos_cursor + 1] not in allowed_vowels) and (word[pos_cursor - 1] not in allowed_vowels):
                return curr_char
        pos_cursor -= 1
    return ""