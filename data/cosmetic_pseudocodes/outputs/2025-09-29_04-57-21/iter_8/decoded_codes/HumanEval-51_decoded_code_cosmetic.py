from typing import Set

def remove_vowels(input_string: str) -> str:
    vowels_set: Set[str] = {"a", "e", "i", "o", "u"}
    result_builder: str = ""
    current_index: int = 0
    length_limit: int = len(input_string)

    while current_index < length_limit:
        letter: str = input_string[current_index]
        lowered: str = letter.lower()
        if lowered not in vowels_set:
            result_builder += letter
        current_index += 1

    return result_builder