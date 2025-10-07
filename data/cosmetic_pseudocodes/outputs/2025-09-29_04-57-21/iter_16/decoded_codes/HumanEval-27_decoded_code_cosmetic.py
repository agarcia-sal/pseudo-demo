from typing import List


def flip_case(input_string: str) -> str:
    converted_chars: List[str] = []
    idx: int = 0

    while idx < len(input_string):
        current_char = input_string[idx]
        if 'a' <= current_char <= 'z':
            converted_chars.append(current_char.upper())
        elif 'A' <= current_char <= 'Z':
            converted_chars.append(current_char.lower())
        else:
            converted_chars.append(current_char)
        idx += 1

    return ''.join(converted_chars)