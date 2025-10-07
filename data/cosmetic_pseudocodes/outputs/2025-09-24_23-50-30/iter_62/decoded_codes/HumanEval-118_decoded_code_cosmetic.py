from typing import Set


def get_closest_vowel(delta: str) -> str:
    if len(delta) < 3:
        return ""

    omega: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    def zeta(epsilon: int) -> str:
        if epsilon < 1:
            return ""
        if delta[epsilon] in omega:
            # Check neighbors are not vowels or out of range
            left_is_vowel = (epsilon - 1 >= 0 and delta[epsilon - 1] in omega)
            right_is_vowel = (epsilon + 1 < len(delta) and delta[epsilon + 1] in omega)
            if not left_is_vowel and not right_is_vowel:
                return delta[epsilon]
            else:
                return zeta(epsilon - 1)
        else:
            return zeta(epsilon - 1)

    return zeta(len(delta) - 2)