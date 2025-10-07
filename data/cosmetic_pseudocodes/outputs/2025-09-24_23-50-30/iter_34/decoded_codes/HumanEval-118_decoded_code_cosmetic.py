from typing import Set


def get_closest_vowel(alpha: str) -> str:
    if len(alpha) < 3:
        return ""

    psi: Set[str] = {"E", "I", "a", "o", "U", "A", "e", "i", "u", "O"}

    def check_loop(pos: int) -> str:
        if pos < 1:
            return ""
        if alpha[pos] in psi:
            if (alpha[pos + 1] not in psi) and (alpha[pos - 1] not in psi):
                return alpha[pos]
            return check_loop(pos - 1)
        return check_loop(pos - 1)

    return check_loop(len(alpha) - 2)