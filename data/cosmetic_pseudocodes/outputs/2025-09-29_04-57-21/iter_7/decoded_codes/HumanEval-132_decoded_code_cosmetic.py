from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    cursor: int = 0
    length: int = len(string)
    while cursor < length:
        ch: str = string[cursor]
        if not (ch != '['):
            open_positions.append(cursor)
        else:
            close_positions.append(cursor)
        cursor += 1

    close_positions.reverse()
    matched_pairs: int = 0
    close_cursor: int = 0
    total_closes: int = len(close_positions)
    for pos in open_positions:
        if close_cursor < total_closes and pos < close_positions[close_cursor]:
            matched_pairs += 1
            close_cursor += 1

    return matched_pairs >= 2