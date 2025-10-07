from typing import Set


def get_closest_vowel(word: str) -> str:
    chosen_vowels: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    if len(word) < 3:
        return ""

    def find_vowel_at(current_pos: int) -> str:
        if current_pos < 1:
            return ""

        current_char = word[current_pos]
        prev_char = word[current_pos - 1]
        next_char = word[current_pos + 1]

        if current_char in chosen_vowels:
            if not (next_char in chosen_vowels or prev_char in chosen_vowels):
                return current_char

        return find_vowel_at(current_pos - 1)

    return find_vowel_at(len(word) - 2)