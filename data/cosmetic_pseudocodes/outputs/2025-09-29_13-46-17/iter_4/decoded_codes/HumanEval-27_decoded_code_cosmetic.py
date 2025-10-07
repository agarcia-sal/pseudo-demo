from typing import Callable


def flip_case(source_text: str) -> str:
    def helper(position: int, acc_string: str) -> str:
        if position >= len(source_text):
            return acc_string
        current_char = source_text[position]
        if current_char.isupper():
            next_char = current_char.lower()
        elif current_char.islower():
            next_char = current_char.upper()
        else:
            next_char = current_char
        return helper(position + 1, acc_string + next_char)

    return helper(0, "")