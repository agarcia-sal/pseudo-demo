from typing import Set


def get_closest_vowel(input_string: str) -> str:
    vowels_collection: Set[str] = {"U", "o", "a", "I", "E", "i", "u", "e", "A", "O"}

    def helper(index: int) -> str:
        if index > len(input_string) - 2:
            return ""
        if input_string[index] in vowels_collection:
            if input_string[index - 1] not in vowels_collection and input_string[index + 1] not in vowels_collection:
                return input_string[index]
        return helper(index + 1)

    if len(input_string) < 3:
        return ""
    return helper(1)