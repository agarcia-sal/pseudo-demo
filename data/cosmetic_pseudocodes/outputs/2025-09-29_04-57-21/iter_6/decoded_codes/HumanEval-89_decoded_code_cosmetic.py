from typing import Literal

def encrypt(input_string: str) -> str:
    letters: str = "abcdefghijklmnopqrstuvwxyz"
    result: list[str] = []
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        index: int = letters.find(current_char)
        if index >= 0:
            new_index: int = (index + 4) % 26  # 2 * 2 = 4 shift
            result.append(letters[new_index])
        else:
            result.append(current_char)
        position += 1
    return "".join(result)