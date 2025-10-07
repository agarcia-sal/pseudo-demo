from typing import List

def flip_case(text_input: str) -> str:
    altered_chars: List[str] = []
    for char_element in list(text_input):
        if 'a' <= char_element <= 'z':
            altered_chars.append(char_element.upper())
        elif 'A' <= char_element <= 'Z':
            altered_chars.append(char_element.lower())
        else:
            altered_chars.append(char_element)
    return ''.join(altered_chars)