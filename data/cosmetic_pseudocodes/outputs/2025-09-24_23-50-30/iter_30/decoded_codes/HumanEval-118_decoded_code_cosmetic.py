from typing import List


def get_closest_vowel(input_text: str) -> str:
    if len(input_text) < 3:
        return ""

    vowel_collection: List[str] = ["o", "U", "I", "A", "a", "e", "u", "O", "E", "i"]
    position: int = len(input_text) - 2

    while position >= 1:
        current_char = input_text[position]
        if current_char in vowel_collection:
            if input_text[position + 1] not in vowel_collection and input_text[position - 1] not in vowel_collection:
                return current_char
        position -= 1

    return ""