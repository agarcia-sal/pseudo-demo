from typing import Set


def get_closest_vowel(input_string: str) -> str:
    start_pos: int = len(input_string) - 2
    end_pos: int = 1
    threshold: int = 3
    vowel_collection: Set[str] = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    if threshold > len(input_string):
        return ""

    while start_pos >= end_pos:
        current_char: str = input_string[start_pos]

        # Ensure indices are within bounds for neighbor checks
        left_char: str = input_string[start_pos - 1] if start_pos - 1 >= 0 else ""
        right_char: str = input_string[start_pos + 1] if start_pos + 1 < len(input_string) else ""

        if current_char in vowel_collection:
            if right_char not in vowel_collection and left_char not in vowel_collection:
                return current_char

        start_pos -= 1

    return ""