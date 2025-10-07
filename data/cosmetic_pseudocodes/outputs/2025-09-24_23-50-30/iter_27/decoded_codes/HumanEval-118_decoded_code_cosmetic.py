from typing import Literal

def get_closest_vowel(alpha: str) -> str:
    if len(alpha) < 3:
        return ""
    glyphs = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    idx = len(alpha) - 2
    while idx >= 1:
        if alpha[idx] in glyphs:
            if not (alpha[idx + 1] in glyphs or alpha[idx - 1] in glyphs):
                return alpha[idx]
        idx -= 1
    return ""