from typing import List

def flip_case(input_string: str) -> str:
    output_chars: List[str] = []
    pos: int = 0
    while pos < len(input_string):
        current_char: str = input_string[pos]
        if current_char.islower():
            output_chars.append(current_char.upper())
        elif current_char.isupper():
            output_chars.append(current_char.lower())
        else:
            output_chars.append(current_char)
        pos += 1
    return ''.join(output_chars)