from typing import Set

def get_closest_vowel(word: str) -> str:
    result: str = ""
    if len(word) < 3:
        return result

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    position: int = len(word) - 2
    while position >= 1:
        current_char = word[position]
        if current_char in vowels:
            next_char = word[position + 1]
            prev_char = word[position - 1]
            if not (next_char in vowels or prev_char in vowels):
                return current_char
        position -= 1
    return result