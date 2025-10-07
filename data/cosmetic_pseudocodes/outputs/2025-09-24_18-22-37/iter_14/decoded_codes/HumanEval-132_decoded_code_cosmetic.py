from typing import List


def is_nested(alpha: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    idx: int = 0
    while idx < len(alpha):
        current_char: str = alpha[idx]
        if current_char == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)
        idx += 1

    close_positions.reverse()
    tally: int = 0
    cursor: int = 0
    close_len: int = len(close_positions)
    for open_elem in open_positions:
        if cursor < close_len:
            if open_elem < close_positions[cursor]:
                tally += 1
                cursor += 1

    return tally >= 2