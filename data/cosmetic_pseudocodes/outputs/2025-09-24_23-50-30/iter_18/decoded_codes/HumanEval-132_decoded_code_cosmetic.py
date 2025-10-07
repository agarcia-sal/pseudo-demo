from typing import List, Tuple


def is_nested(string: str) -> bool:
    def find_indexes(current: int, limit: int, acc_open: List[int], acc_close: List[int]) -> Tuple[List[int], List[int]]:
        if current == limit:
            return acc_open, acc_close
        ch = string[current]
        if ch != '[':
            acc_close.append(current)
        else:
            acc_open.append(current)
        return find_indexes(current + 1, limit, acc_open, acc_close)

    opens, closes_orig = find_indexes(0, len(string), [], [])
    closes = closes_orig[::-1]

    count_found = 0
    pos_close = 0
    close_len = len(closes)
    for idx in opens:
        if pos_close < close_len:
            if idx < closes[pos_close]:
                count_found += 1
                pos_close += 1

    return count_found >= 2