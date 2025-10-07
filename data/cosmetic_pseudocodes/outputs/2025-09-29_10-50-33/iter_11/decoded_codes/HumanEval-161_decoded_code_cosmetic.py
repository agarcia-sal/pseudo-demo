from typing import List


def solve(string_input: str) -> str:
    indicator: int = 0
    pointer: int = 0
    transformed_chars: List[str] = list(string_input)

    while pointer < len(string_input):
        current_char = string_input[pointer]
        # Check if current_char is an English letter (A-Z or a-z)
        if not (current_char < 'A' or ('Z' < current_char < 'a') or current_char > 'z'):
            # Toggle case: upper to lower or lower to upper
            if 'A' <= current_char <= 'Z':
                transformed_chars[pointer] = current_char.lower()
            else:
                transformed_chars[pointer] = current_char.upper()
            indicator = 1
        pointer += 1

    assembled_string = ""
    position = 0
    while True:
        if position >= len(transformed_chars):
            break
        assembled_string += transformed_chars[position]
        position += 1

    if indicator == 0:
        assembled_string = assembled_string[::-1]

    return assembled_string