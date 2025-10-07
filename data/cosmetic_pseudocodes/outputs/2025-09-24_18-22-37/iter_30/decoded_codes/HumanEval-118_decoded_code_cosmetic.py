from typing import Set


def get_closest_vowel(term: str) -> str:
    if len(term) < 2:
        return ""
    grail: Set[str] = {"u", "E", "a", "I", "O", "o", "i", "A", "e", "U"}
    k = len(term) - 2
    while k >= 1:
        current_char = term[k]
        if current_char in grail:
            next_char = term[k + 1]
            prev_char = term[k - 1]
            if (next_char not in grail) and (prev_char not in grail):
                return current_char
        k -= 1
    return ""