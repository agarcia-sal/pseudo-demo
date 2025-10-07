from typing import List


def is_nested(str_param: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    for idx, current_char in enumerate(str_param):
        if current_char == '[':
            open_positions.append(idx)
        else:
            close_positions.append(idx)

    close_positions.reverse()

    matched_count = 0
    close_pos_ptr = 0
    total_closes = len(close_positions)

    for current_open in open_positions:
        if close_pos_ptr < total_closes:
            current_close = close_positions[close_pos_ptr]
            if current_open < current_close:
                matched_count += 1
                close_pos_ptr += 1

    return matched_count >= 2