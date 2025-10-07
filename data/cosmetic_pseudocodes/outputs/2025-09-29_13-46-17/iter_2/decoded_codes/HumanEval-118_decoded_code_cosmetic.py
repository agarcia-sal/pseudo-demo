from typing import Set


def get_closest_vowel(word: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    def check_pos(pos: int) -> str:
        if pos < 1:
            return ""
        if word[pos] in vowels:
            if word[pos + 1] not in vowels and word[pos - 1] not in vowels:
                return word[pos]
            return check_pos(pos - 1)
        return check_pos(pos - 1)

    if len(word) < 3:
        return ""
    return check_pos(len(word) - 2)