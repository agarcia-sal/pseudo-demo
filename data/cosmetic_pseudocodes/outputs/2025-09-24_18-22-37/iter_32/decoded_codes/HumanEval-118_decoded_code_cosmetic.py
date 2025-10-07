from typing import Set


def get_closest_vowel(word: str) -> str:
    n: int = len(word)
    if n < 3:
        return ""

    letters: Set[str] = {"e", "u", "a", "I", "E", "A", "o", "O", "i", "U"}

    k: int = n - 2
    while k >= 1:
        candidate = word[k]
        if candidate in letters:
            if (word[k + 1] not in letters) and (word[k - 1] not in letters):
                return candidate
        k -= 1

    return ""