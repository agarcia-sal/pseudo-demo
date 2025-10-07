from typing import Set


def get_closest_vowel(word: str) -> str:
    vowels_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    lenw: int = len(word)
    if lenw < 3:
        return ""

    def inner_search(pos: int) -> str:
        if pos < 1:
            return ""
        c = word[pos]
        prev_c = word[pos - 1]
        next_c = word[pos + 1]
        is_current_vowel = c in vowels_set
        is_prev_vowel = prev_c in vowels_set
        is_next_vowel = next_c in vowels_set
        if is_current_vowel:
            if (is_prev_vowel + is_next_vowel) == 0:
                return c
            else:
                return inner_search(pos - 1)
        else:
            return inner_search(pos - 1)

    result = inner_search(lenw - 2)
    return result