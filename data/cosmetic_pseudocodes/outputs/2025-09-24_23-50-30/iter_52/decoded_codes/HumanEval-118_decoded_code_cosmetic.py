from typing import Set

def get_closest_vowel(alpha: str) -> str:
    if len(alpha) <= 2:
        return ""

    glyphs: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def search(pos: int) -> str:
        if pos < 1:
            return ""
        if alpha[pos] in glyphs:
            if alpha[pos + 1] not in glyphs and alpha[pos - 1] not in glyphs:
                return alpha[pos]
        return search(pos - 1)

    return search(len(alpha) - 2)