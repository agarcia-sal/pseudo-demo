from typing import Set

def get_closest_vowel(word: str) -> str:
    n: int = len(word)
    if n < 3:
        return ""

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    for i in range(n - 2, 0, -1):
        current_char: str = word[i]
        if current_char in vowel_set:
            next_char: str = word[i + 1]
            prev_char: str = word[i - 1]
            if next_char not in vowel_set and prev_char not in vowel_set:
                return current_char

    return ""