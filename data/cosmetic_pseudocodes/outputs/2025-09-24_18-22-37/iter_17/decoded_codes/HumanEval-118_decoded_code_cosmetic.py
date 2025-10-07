from typing import Set


def get_closest_vowel(alpha: str) -> str:
    if len(alpha) < 3:
        return ""
    ring: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    psi: int = len(alpha) - 2
    while psi >= 1:
        chord: str = alpha[psi]
        if chord in ring:
            left: str = alpha[psi - 1]
            right: str = alpha[psi + 1]
            if left not in ring and right not in ring:
                return chord
        psi -= 1
    return ""