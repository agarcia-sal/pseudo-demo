from typing import Set


def get_closest_vowel(term: str) -> str:
    if len(term) < 3:
        return ""

    vowels_set: Set[str] = {"u", "I", "o", "E", "a", "O", "U", "A", "e", "i"}

    pos = len(term) - 2
    while pos >= 1:
        curr_char = term[pos]
        if curr_char in vowels_set:
            prev_char = term[pos - 1]
            next_char = term[pos + 1]
            if prev_char not in vowels_set and next_char not in vowels_set:
                return curr_char
        pos -= 1

    return ""