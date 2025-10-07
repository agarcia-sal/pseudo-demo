from typing import Set


def remove_vowels(input_string: str) -> str:
    vowels_set: Set[str] = {"a", "e", "i", "o", "u"}
    result_string: str = "".join(
        character for character in input_string if character.lower() not in vowels_set
    )
    return result_string