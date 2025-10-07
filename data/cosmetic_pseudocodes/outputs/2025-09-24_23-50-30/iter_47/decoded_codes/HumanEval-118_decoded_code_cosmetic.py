from typing import List

def get_closest_vowel(input_string: str) -> str:
    if len(input_string) < 3:
        return ""

    vowel_set: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    position: int = len(input_string) - 2
    while position >= 1:
        if input_string[position] in vowel_set:
            if (input_string[position + 1] not in vowel_set) and (input_string[position - 1] not in vowel_set):
                return input_string[position]
        position -= 1

    return ""