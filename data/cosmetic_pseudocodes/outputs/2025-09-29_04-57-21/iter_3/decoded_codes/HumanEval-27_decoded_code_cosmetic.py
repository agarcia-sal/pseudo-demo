from typing import List

def flip_case(text_input: str) -> str:
    transformed_chars: List[str] = []
    for single_char in text_input:
        if single_char.isupper():
            transformed_chars.append(single_char.lower())
        elif single_char.islower():
            transformed_chars.append(single_char.upper())
        else:
            transformed_chars.append(single_char)
    return ''.join(transformed_chars)