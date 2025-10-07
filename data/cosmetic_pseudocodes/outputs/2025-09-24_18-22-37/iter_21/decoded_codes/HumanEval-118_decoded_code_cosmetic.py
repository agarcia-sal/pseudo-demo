from typing import Set

def get_closest_vowel(text: str) -> str:
    if len(text) < 3:
        return ""

    vowel_set: Set[str] = {"u", "E", "a", "I", "o", "A", "i", "U", "O", "e"}

    pos: int = len(text) - 2
    while pos >= 1:
        current_char: str = text[pos]
        if current_char in vowel_set:
            right_char: str = text[pos + 1]
            left_char: str = text[pos - 1]
            if right_char not in vowel_set and left_char not in vowel_set:
                return current_char
        pos -= 1

    return ""