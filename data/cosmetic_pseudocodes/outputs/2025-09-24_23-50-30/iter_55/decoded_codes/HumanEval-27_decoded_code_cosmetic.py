from typing import Callable

def flip_case(transform_string: str) -> str:
    def toggle_case_at(index: int, acc: str) -> str:
        if index == len(transform_string):
            return acc
        current_char = transform_string[index]
        switched_char = current_char.lower() if current_char == current_char.upper() else current_char.upper()
        return toggle_case_at(index + 1, acc + switched_char)
    return toggle_case_at(0, "")