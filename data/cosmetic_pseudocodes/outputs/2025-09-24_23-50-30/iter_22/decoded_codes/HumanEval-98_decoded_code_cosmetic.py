from typing import List


def count_upper(string_input: str) -> int:
    accumulator: int = 0
    positions: List[int] = []
    position_index: int = 0

    while position_index < len(string_input):
        if position_index % 2 == 0:
            positions.append(position_index)
        position_index += 1

    iterator: int = 0
    while iterator < len(positions):
        char_candidate: str = string_input[positions[iterator]]
        if char_candidate in {'A', 'E', 'I', 'O', 'U'}:
            accumulator += 1
        iterator += 1

    return accumulator