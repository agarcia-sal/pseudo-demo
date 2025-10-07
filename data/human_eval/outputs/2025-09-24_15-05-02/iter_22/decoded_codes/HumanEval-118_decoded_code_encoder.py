from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""
    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for index in range(len(word) - 2, 0, -1):
        if word[index] in vowel_set:
            if word[index + 1] not in vowel_set and word[index - 1] not in vowel_set:
                return word[index]
    return ""