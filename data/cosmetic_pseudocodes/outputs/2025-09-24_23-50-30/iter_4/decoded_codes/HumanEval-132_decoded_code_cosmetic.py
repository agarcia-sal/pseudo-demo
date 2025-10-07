from typing import List, Tuple


def is_nested(string: str) -> bool:
    def get_brackets(pos: int = 0, opens: List[int] = [], closes: List[int] = []) -> Tuple[List[int], List[int]]:
        if pos == len(string):
            return opens, closes
        char = string[pos]
        new_opens = opens + [pos] if char == '[' else opens
        new_closes = closes + [pos] if char != '[' else closes
        return get_brackets(pos + 1, new_opens, new_closes)

    open_positions, close_positions = get_brackets()
    close_positions = close_positions[::-1]

    def count_pairs(open_list: List[int], close_list: List[int], count: int = 0, idx: int = 0) -> int:
        if not open_list or idx == len(close_list):
            return count
        if open_list[0] < close_list[idx]:
            return count_pairs(open_list[1:], close_list, count + 1, idx + 1)
        else:
            return count_pairs(open_list[1:], close_list, count, idx)

    return count_pairs(open_positions, close_positions) >= 2