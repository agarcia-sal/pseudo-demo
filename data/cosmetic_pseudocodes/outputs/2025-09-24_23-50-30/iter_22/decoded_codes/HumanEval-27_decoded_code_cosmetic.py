from typing import List

def flip_case(string_input: str) -> str:
    modified_chars: List[str] = []
    position: int = 0
    while position < len(string_input):
        current: str = string_input[position]
        if current.isupper():
            modified_chars.append(current.lower())
        elif current.islower():
            modified_chars.append(current.upper())
        else:
            modified_chars.append(current)
        position += 1
    return ''.join(modified_chars)