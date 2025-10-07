from typing import Dict


def get_closest_vowel(alpha: str) -> str:
    if len(alpha) < 3:
        return ""

    vowel_set: Dict[str, bool] = {ch: True for ch in "aeiouAEIOU"}

    def search(pos: int) -> str:
        if pos == 0:
            return ""
        if alpha[pos] in vowel_set:
            left_vowel = alpha[pos - 1] in vowel_set if pos - 1 >= 0 else False
            right_vowel = alpha[pos + 1] in vowel_set if pos + 1 < len(alpha) else False
            if not left_vowel and not right_vowel:
                return alpha[pos]
        return search(pos - 1)

    return search(len(alpha) - 2)