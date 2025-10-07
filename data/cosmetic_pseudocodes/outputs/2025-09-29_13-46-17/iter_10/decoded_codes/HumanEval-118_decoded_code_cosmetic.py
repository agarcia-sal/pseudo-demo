from typing import Set

def get_closest_vowel(word: str) -> str:
    closest_vowel: str = " "
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def find_closest_vowel() -> int:
        # Iterate indices from len(word) - 2 down to 1 inclusive
        for i in range(len(word) - 2, 0, -1):
            current, next_char, prev_char = word[i], word[i + 1], word[i - 1]
            if current in vowels:
                if (next_char not in vowels) and (prev_char not in vowels):
                    nonlocal closest_vowel
                    closest_vowel = current
                    return -1
        return 0

    find_closest_vowel()

    if len(word) < 3:
        return " "
    else:
        return closest_vowel