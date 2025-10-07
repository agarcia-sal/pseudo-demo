from typing import Literal


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    pos = len(word) - 2
    while pos >= 1:
        if word[pos] in vowel_set:
            if (word[pos + 1] in vowel_set) or (word[pos - 1] in vowel_set):
                pos -= 1
                continue
            else:
                return word[pos]
        pos -= 1
    return ""