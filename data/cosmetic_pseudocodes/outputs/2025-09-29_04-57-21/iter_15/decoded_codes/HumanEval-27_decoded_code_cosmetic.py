from typing import List


def flip_case(input_string: str) -> str:
    def toggle_case(character: str) -> str:
        if not ('a' <= character <= 'z'):
            if 'A' <= character <= 'Z':
                return character.lower()
            return character
        else:
            return character.upper()

    transformed_chars: List[str] = []
    index: int = 0
    while index < len(input_string):
        transformed_chars.append(toggle_case(input_string[index]))
        index += 1

    return "".join(transformed_chars)