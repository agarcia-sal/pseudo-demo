from typing import List

def flip_case(text_argument: str) -> str:
    transformed_chars: List[str] = []
    for index in range(len(text_argument)):
        current_char = text_argument[index]
        if current_char.islower():
            transformed_chars.append(current_char.upper())
        elif current_char.isupper():
            transformed_chars.append(current_char.lower())
        else:
            transformed_chars.append(current_char)
    return ''.join(transformed_chars)