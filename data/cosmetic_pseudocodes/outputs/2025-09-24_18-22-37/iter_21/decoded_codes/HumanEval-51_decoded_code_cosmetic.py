from typing import List

def remove_vowels(input_string: str) -> str:
    output_string: str = ""
    vowels_list: List[str] = ["a", "e", "i", "o", "u"]
    position: int = 0
    while True:
        if position >= len(input_string):
            break
        current_char: str = input_string[position]
        lowered_char: str = current_char.lower()
        if lowered_char in vowels_list:
            pass
        else:
            output_string += current_char
        position += 1
    return output_string