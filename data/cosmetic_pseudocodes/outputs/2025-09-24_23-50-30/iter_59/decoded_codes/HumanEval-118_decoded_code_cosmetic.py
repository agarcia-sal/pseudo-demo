from typing import Sequence


def hz_check_element(qg: Sequence[str], qk: int, zx: set[str]) -> bool:
    # Return True if qg[qk] is a vowel, else False
    if 0 <= qk < len(qg):
        c = qg[qk]
        return c in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    return False


def get_closest_vowel(br: Sequence[str]) -> str:
    if len(br) <= 2:
        return ""

    zx = {"u", "o", "A", "O", "a", "I", "i", "U", "E", "e"}

    hj = len(br) - 2
    while hj >= 1:
        if hz_check_element(br, hj, zx):
            if not hz_check_element(br, hj + 1, zx) and not hz_check_element(br, hj - 1, zx):
                return br[hj]
        hj -= 1

    return ""