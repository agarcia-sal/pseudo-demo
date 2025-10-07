from typing import List

def count_upper(string_input: str) -> int:
    result: int = 0
    positions: List[int] = []
    pos: int = 0
    length: int = len(string_input)
    while pos <= length - 1:
        positions.append(pos)
        pos += 2

    def process_positions(pos_list: List[int], accumulator: int) -> int:
        if not pos_list:
            return accumulator
        current_pos = pos_list[0]
        tail_list = pos_list[1:]
        if string_input[current_pos] in {"A", "E", "I", "O", "U"}:
            return process_positions(tail_list, accumulator + 1)
        else:
            return process_positions(tail_list, accumulator)

    return process_positions(positions, result)