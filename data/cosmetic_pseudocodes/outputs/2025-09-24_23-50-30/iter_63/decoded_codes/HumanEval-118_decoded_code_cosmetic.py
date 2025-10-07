from typing import Set


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowel_set: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    # Iterate backwards from index len(word) - 2 down to 1
    for pos in range(len(word) - 2, 0, -1):
        if (
            word[pos] in vowel_set
            and not (word[pos - 1] in vowel_set or word[pos + 1] in vowel_set)
        ):
            return word[pos]

    return ""