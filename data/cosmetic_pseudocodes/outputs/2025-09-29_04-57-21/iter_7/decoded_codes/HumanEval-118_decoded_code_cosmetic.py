from typing import Literal

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    melody_chars = {"A", "I", "O", "U", "E", "a", "u", "e", "o", "i"}
    pos = len(word) - 2
    while pos >= 1:
        if word[pos] in melody_chars:
            if word[pos + 1] not in melody_chars and word[pos - 1] not in melody_chars:
                return word[pos]
        pos -= 1
    return ""