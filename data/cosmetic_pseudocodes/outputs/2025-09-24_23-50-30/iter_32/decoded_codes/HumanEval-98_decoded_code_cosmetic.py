from typing import Sequence

def count_upper(raw_sequence: Sequence[str]) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < len(raw_sequence):
        if raw_sequence[iterator] in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1
        iterator += 2
    return accumulator