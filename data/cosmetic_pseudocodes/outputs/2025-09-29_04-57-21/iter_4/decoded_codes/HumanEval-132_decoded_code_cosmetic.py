from typing import List


def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    cursor: int = 0
    text_length: int = len(string)

    while cursor != text_length:
        current_char: str = string[cursor]
        if current_char == '[':
            open_positions.append(cursor)
        else:
            close_positions.append(cursor)
        cursor += 1

    i: int = 0
    j: int = len(close_positions) - 1
    matched_pairs: int = 0

    while j >= 0:
        if i < len(open_positions):
            k = open_positions[i]
            l = close_positions[j]
            if k < l:
                matched_pairs += 1
                i += 1
                j -= 1
                continue
        j -= 1

    return matched_pairs >= 2