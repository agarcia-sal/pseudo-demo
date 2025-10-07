from typing import Set


def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    # Iterate from second last character to second character
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            # Ensure both neighbors are consonants (not vowels)
            if (word[i + 1] not in vowels) and (word[i - 1] not in vowels):
                return word[i]

    return ""