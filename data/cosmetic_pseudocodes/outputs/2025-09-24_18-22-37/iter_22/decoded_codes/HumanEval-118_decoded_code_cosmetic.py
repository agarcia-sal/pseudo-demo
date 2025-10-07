from typing import Set

def get_closest_vowel(input_string: str) -> str:
    if len(input_string) < 3:
        return ""
    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    position = len(input_string) - 2  # len(input_string) - (1 + 1)

    while position >= 1:
        if input_string[position] in vowel_set:
            if not (input_string[position + 1] in vowel_set or input_string[position - 1] in vowel_set):
                return input_string[position]
        position -= 1

    return ""