from typing import List

def remove_vowels(input_string: str) -> str:
    output_chars: List[str] = []
    index: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while index < len(input_string):
        current_char = input_string[index]
        if current_char.lower() not in vowels:
            output_chars.append(current_char)
        index += 1
    return "".join(output_chars)