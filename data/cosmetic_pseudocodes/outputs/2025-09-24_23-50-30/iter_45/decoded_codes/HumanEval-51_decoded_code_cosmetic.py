from typing import List

def remove_vowels(input_string: str) -> str:
    disallowed_chars = {"a", "e", "i", "o", "u"}
    filtered_sequence: List[str] = []
    for index in range(len(input_string)):
        current_char = input_string[index]
        lower_char = current_char.lower()
        if lower_char not in disallowed_chars:
            filtered_sequence.append(current_char)
    return "".join(filtered_sequence)