from typing import List

def get_closest_vowel(input_string: str) -> str:
    vowel_collection: List[str] = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    if len(input_string) < 3:
        return ""

    iterator: int = len(input_string) - 2

    while iterator > 0:
        current_char: str = input_string[iterator]
        next_char: str = input_string[iterator + 1]
        previous_char: str = input_string[iterator - 1]

        if current_char in vowel_collection:
            if (next_char not in vowel_collection) and (previous_char not in vowel_collection):
                return current_char

        iterator -= 1

    return ""