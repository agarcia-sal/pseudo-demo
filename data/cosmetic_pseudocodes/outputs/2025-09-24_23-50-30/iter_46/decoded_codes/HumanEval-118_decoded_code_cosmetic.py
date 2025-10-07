from typing import Set


def get_closest_vowel(alp: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def rec_scan(pos: int) -> str:
        if pos <= 0:
            return ""
        if alp[pos] in vowels:
            left_is_vowel = alp[pos - 1] in vowels if pos - 1 >= 0 else False
            right_is_vowel = alp[pos + 1] in vowels if pos + 1 < len(alp) else False
            if not right_is_vowel and not left_is_vowel:
                return alp[pos]
            return rec_scan(pos - 1)
        return rec_scan(pos - 1)

    if len(alp) < 3:
        return ""
    return rec_scan(len(alp) - 2)