from typing import List

def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    iterator: int = 0

    while iterator < len(string):
        if string[iterator] == '[':
            open_positions.append(iterator)
        else:
            close_positions.append(iterator)
        iterator += 1

    close_positions.reverse()

    matched_count: int = 0
    close_index: int = 0
    total_close: int = len(close_positions)

    for open_index in open_positions:
        if not (close_index >= total_close or open_index >= close_positions[close_index]):
            matched_count += 1
            close_index += 1

    return not (matched_count < 2)