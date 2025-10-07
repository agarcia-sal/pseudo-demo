from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    for index in range(len(word) - 2, 0, -1):
        c = word[index]
        if c in vowels:
            if word[index + 1] not in vowels and word[index - 1] not in vowels:
                return c

    return ""