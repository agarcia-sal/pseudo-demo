from typing import Callable

def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result: list[str] = []

    def process_characters(position: int) -> None:
        if position == len(input_string):
            return
        current: str = input_string[position]
        if current in letters:
            base_pos: int = letters.index(current)
            transformed_pos: int = ((base_pos + 2) * 2) % 26
            new_char: str = letters[transformed_pos]
            result.append(new_char)
        else:
            result.append(current)
        process_characters(position + 1)

    process_characters(0)
    return ''.join(result)