from typing import Literal

def count_upper(input_str: str) -> int:
    accumulator: int = 0
    pos: int = 0
    while pos < len(input_str):
        ch: Literal['A', 'E', 'I', 'O', 'U', 'Other'] = (
            input_str[pos] if input_str[pos] in {'A', 'E', 'I', 'O', 'U'} else 'Other'
        )
        if ch != 'Other':
            accumulator += 1
        pos += 2
    return accumulator