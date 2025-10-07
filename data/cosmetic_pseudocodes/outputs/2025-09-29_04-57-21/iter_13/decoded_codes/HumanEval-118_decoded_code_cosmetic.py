from typing import Set

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def check_positions(position: int) -> str:
        if position < 1:
            return ""
        if word[position] not in vowel_set:
            return check_positions(position - 1)
        # Ensure no adjacent vowels
        if word[position + 1] in vowel_set or word[position - 1] in vowel_set:
            return check_positions(position - 1)
        return word[position]

    return check_positions(len(word) - 2)