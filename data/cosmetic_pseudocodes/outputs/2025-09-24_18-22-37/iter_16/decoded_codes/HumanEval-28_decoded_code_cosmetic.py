from typing import Sequence

def concatenate(qwerty: Sequence[str]) -> str:
    result_string: str = ""
    iterator_index: int = 0
    while iterator_index < len(qwerty):
        current_piece: str = qwerty[iterator_index]
        result_string += current_piece
        iterator_index += 1
    return result_string