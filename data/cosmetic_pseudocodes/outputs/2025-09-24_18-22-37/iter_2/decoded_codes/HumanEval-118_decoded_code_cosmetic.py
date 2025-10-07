from typing import Set

def get_closest_vowel(word: str) -> str:
    vowels_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if len(word) < 3:
        return ""
    pos: int = len(word) - 2
    while pos >= 1:
        current_char: str = word[pos]
        if current_char in vowels_set:
            before_char: str = word[pos - 1]
            after_char: str = word[pos + 1]
            if before_char not in vowels_set and after_char not in vowels_set:
                return current_char
        pos -= 1
    return ""