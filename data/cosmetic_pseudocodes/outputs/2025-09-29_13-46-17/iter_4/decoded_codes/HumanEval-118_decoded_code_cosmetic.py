from typing import Set


def get_closest_vowel(word: str) -> str:
    VOWELS_SET: Set[str] = {"O", "U", "a", "E", "e", "A", "I", "i", "o", "u"}

    def search(position: int) -> str:
        if position < 1:
            return ""
        # Check if neighbors are not vowels
        if (word[position + 1] not in VOWELS_SET) and (word[position - 1] not in VOWELS_SET):
            if word[position] in VOWELS_SET:
                return word[position]
        return search(position - 1)

    if len(word) < 3:
        return ""
    return search(len(word) - 2)