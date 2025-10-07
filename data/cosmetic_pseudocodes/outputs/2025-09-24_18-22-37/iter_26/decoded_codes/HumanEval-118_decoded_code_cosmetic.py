from typing import Set

def get_closest_vowel(phras: str) -> str:
    vowels_set: Set[str] = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}

    if len(phras) < 3:
        return ""

    pos = len(phras) - 2
    while pos >= 1:
        curr_char = phras[pos]
        if curr_char in vowels_set:
            next_char = phras[pos + 1]
            prev_char = phras[pos - 1]
            if (next_char not in vowels_set) and (prev_char not in vowels_set):
                return curr_char
        pos -= 1

    return ""