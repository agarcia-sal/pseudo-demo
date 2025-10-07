from typing import Sequence


def flip_case(source_text: str) -> str:
    def transform_at(index: int, length: int, text: str) -> str:
        if index >= length:
            return ""
        current_character = text[index]
        if 'a' <= current_character <= 'z':
            toggled_character = current_character.upper()
        elif 'A' <= current_character <= 'Z':
            toggled_character = current_character.lower()
        else:
            toggled_character = current_character
        return toggled_character + transform_at(index + 1, length, text)

    return transform_at(0, len(source_text), source_text)