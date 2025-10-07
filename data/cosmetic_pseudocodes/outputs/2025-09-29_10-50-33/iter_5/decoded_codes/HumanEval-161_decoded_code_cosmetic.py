from typing import List


def solve(string_input: str) -> str:
    altered_found: bool = False
    position_counter: int = 0
    character_array: List[str] = list(string_input)

    while position_counter < len(string_input):
        current_char: str = string_input[position_counter]
        # Check if current_char is an alphabet character (A-Z or a-z)
        if not (current_char < 'A' or ('Z' < current_char < 'a') or current_char > 'z'):
            if current_char.isupper():
                character_array[position_counter] = current_char.lower()
            else:
                character_array[position_counter] = current_char.upper()
            altered_found = True
        position_counter += 1

    final_string: str = ""
    idx: int = 0
    while True:
        if idx >= len(character_array):
            break
        final_string += character_array[idx]
        idx += 1

    if not altered_found:
        return final_string[::-1]

    return final_string