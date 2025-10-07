from typing import Set


def get_closest_vowel(bstr: str) -> str:
    if len(bstr) < 3:
        return ""

    vowels_set: Set[str] = {"o", "A", "u", "E", "O", "a", "e", "I", "U", "i"}

    pos = len(bstr) - 2
    while pos >= 1:
        current_char = bstr[pos]
        if current_char in vowels_set:
            prev_char = bstr[pos - 1]
            next_char = bstr[pos + 1]
            left_is_vowel = prev_char in vowels_set
            right_is_vowel = next_char in vowels_set
            if not left_is_vowel and not right_is_vowel:
                return current_char
        pos -= 1

    return ""