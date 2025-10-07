from typing import List


def is_nested(input_text: str) -> bool:
    start_positions: List[int] = []
    end_positions: List[int] = []
    cursor: int = 0
    length: int = len(input_text)

    while cursor <= length - 1:
        current_char: str = input_text[cursor]
        if current_char == '[':
            start_positions.append(cursor)
        else:
            end_positions.append(cursor)
        cursor += 1

    end_positions.reverse()

    matched_brackets: int = 0
    end_index: int = 0
    total_end: int = len(end_positions)

    for start_pos in start_positions:
        if end_index < total_end and start_pos < end_positions[end_index]:
            matched_brackets += 1
            end_index += 1

    return matched_brackets >= 2