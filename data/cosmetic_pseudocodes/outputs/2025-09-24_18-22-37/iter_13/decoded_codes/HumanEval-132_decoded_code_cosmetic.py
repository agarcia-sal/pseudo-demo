from typing import List


def is_nested(string_param: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []
    curr_idx: int = 0
    length: int = len(string_param)
    # Separate positions of '[' and any other character, presumed ']'
    while curr_idx < length:
        if string_param[curr_idx] == '[':
            open_positions.append(curr_idx)
        else:
            close_positions.append(curr_idx)
        curr_idx += 1

    reversed_close_positions: List[int] = []
    idx_for_close: int = len(close_positions) - 1
    # Reverse close_positions without using reversed()
    while idx_for_close >= 0:
        reversed_close_positions.append(close_positions[idx_for_close])
        idx_for_close -= 1

    matched_count: int = 0
    pointer: int = 0
    total_closes: int = len(reversed_close_positions)
    # Count matches where open_pos < reversed close position
    for open_pos in open_positions:
        if pointer < total_closes and open_pos < reversed_close_positions[pointer]:
            matched_count += 1
            pointer += 1

    return matched_count >= 2