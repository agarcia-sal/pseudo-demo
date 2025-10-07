from typing import List

def is_nested(string: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    for i in range(len(string)):
        if string[i] == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)

    reversed_closes: List[int] = close_positions[::-1]

    matched_pairs: int = 0
    close_index: int = 0
    total_closes: int = len(reversed_closes)

    for open_pos in open_positions:
        if close_index < total_closes and open_pos < reversed_closes[close_index]:
            matched_pairs += 1
            close_index += 1

    return matched_pairs >= 2