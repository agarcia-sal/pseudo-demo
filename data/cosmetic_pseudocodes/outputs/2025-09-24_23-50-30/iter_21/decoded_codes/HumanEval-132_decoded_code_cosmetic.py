from typing import List, Tuple


def is_nested(input_str: str) -> bool:
    def collect_brackets(pos: int, open_list: List[int], close_list: List[int]) -> Tuple[List[int], List[int]]:
        if pos == len(input_str):
            return open_list, close_list
        if input_str[pos] == '[':
            return collect_brackets(pos + 1, open_list + [pos], close_list)
        else:
            return collect_brackets(pos + 1, open_list, close_list + [pos])

    opens, closes = collect_brackets(0, [], [])
    reversed_closes = closes[::-1]  # reversed list of close positions

    hit_count = 0
    idx_close = 0
    max_close = len(reversed_closes)

    for open_pos in opens:
        if idx_close < max_close and open_pos < reversed_closes[idx_close]:
            hit_count += 1
            idx_close += 1

    return hit_count >= 2