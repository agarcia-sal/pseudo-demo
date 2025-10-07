from typing import List


def remove_vowels(input_string: str) -> str:
    character_array: List[str] = []
    idx: int = 0

    while idx < len(input_string):
        current_character: str = input_string[idx]
        lowered_character: str = current_character

        if "A" <= lowered_character <= "Z":
            # convert uppercase ASCII to lowercase
            lowercase_character = chr(ord(lowered_character) + (ord("a") - ord("A")))
        else:
            lowercase_character = lowered_character

        if lowercase_character in ("a", "e", "i", "o", "u"):
            # skip vowels
            pass
        else:
            character_array.append(current_character)

        idx += 1

    result_string: str = ""
    pos: int = 0

    while pos < len(character_array):
        result_string += character_array[pos]
        pos += 1

    return result_string