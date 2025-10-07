from typing import Callable

def encrypt(input_string: str) -> str:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    def process(position: int) -> None:
        if position >= len(input_string):
            return
        current_char = input_string[position]
        if current_char not in letters:
            result.append(current_char)
            process(position + 1)
            return
        original_pos = letters.index(current_char)
        transformed_pos = (4 * original_pos) % 26  # (2*2)*original_pos
        result.append(letters[transformed_pos])
        process(position + 1)

    process(0)
    return ''.join(result)