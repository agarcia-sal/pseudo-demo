from functools import reduce
from typing import List


def is_nested(input_seq: str) -> bool:
    def accumulate_open_positions(idx: int, acc: List[int]) -> List[int]:
        if idx >= len(input_seq) - 1:
            return acc
        if input_seq[idx] == '[':
            return accumulate_open_positions(idx + 1, acc + [idx])
        return accumulate_open_positions(idx + 1, acc)

    def accumulate_close_positions(idx: int, acc: List[int]) -> List[int]:
        if idx > len(input_seq) - 1:
            return acc
        if input_seq[idx] != '[':
            return accumulate_close_positions(idx + 1, acc + [idx])
        return accumulate_close_positions(idx + 1, acc)

    positions_open = accumulate_open_positions(0, [])
    positions_close = accumulate_close_positions(0, [])
    positions_close = reduce(lambda acc, val: [val] + acc, positions_close, [])

    def count_valid_pairs(i_open: int, i_close: int, acc_count: int) -> int:
        if i_open >= len(positions_open) or i_close >= len(positions_close):
            return acc_count
        if positions_open[i_open] < positions_close[i_close]:
            return count_valid_pairs(i_open + 1, i_close + 1, acc_count + 1)
        return count_valid_pairs(i_open + 1, i_close, acc_count)

    total_pairs = count_valid_pairs(0, 0, 0)
    return not (total_pairs < 2)