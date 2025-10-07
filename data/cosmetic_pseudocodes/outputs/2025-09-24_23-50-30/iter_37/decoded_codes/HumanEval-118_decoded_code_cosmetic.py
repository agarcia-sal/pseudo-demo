from typing import Set

def get_closest_vowel(text: str) -> str:
    if len(text) < 3:
        return ""

    vowel_set: Set[str] = {"I", "A", "O", "U", "E", "i", "u", "o", "a", "e"}

    position = len(text) - 2

    while position >= 1:
        # Checking position is always in the desired range: 1 <= position <= len(text) - 2
        # This condition is redundant based on loop but kept to match pseudocode
        if 1 <= position <= len(text) - 2:
            if text[position] in vowel_set:
                if text[position + 1] not in vowel_set and text[position - 1] not in vowel_set:
                    return text[position]
        position -= 1

    return ""