from typing import List

def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    current_index: int = 0

    while current_index < len(string):
        if string[current_index] == '[':
            open_positions.append(current_index)
        else:
            close_positions.append(current_index)
        current_index += 1

    close_positions.reverse()
    matched: int = 0
    pointer: int = 0
    close_len: int = len(close_positions)

    for open_pos in open_positions:
        if pointer < close_len and open_pos < close_positions[pointer]:
            matched += 1
            pointer += 1

    return matched >= 2