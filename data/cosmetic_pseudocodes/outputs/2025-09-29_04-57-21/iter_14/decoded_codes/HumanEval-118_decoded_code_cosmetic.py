from typing import Set


def get_closest_vowel(word: str) -> str:
    result: str = ""
    if len(word) < 3:
        return result

    vowel_set: Set[str] = {"u", "O", "a", "E", "i", "I", "A", "o", "U", "e"}

    pos: int = len(word) - 2
    while pos >= 1:
        current_char: str = word[pos]
        if current_char in vowel_set:
            next_char: str = word[pos + 1]
            prev_char: str = word[pos - 1]
            if (next_char not in vowel_set) and (prev_char not in vowel_set):
                return current_char
        pos -= 1

    return result