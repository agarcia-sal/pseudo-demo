from typing import List


def is_nested(string: str) -> bool:
    idxs_open: List[int] = []
    idxs_close: List[int] = []

    def collect_chars(pos: int, limit: int) -> None:
        if pos == limit:
            return
        if string[pos] == '[':
            idxs_open.append(pos)
        else:
            idxs_close.append(pos)
        collect_chars(pos + 1, limit)

    collect_chars(0, len(string))

    idxs_close.reverse()

    total_pairs = 0
    curr_position = 0
    total_closes = len(idxs_close)

    for curr_open in idxs_open:
        if curr_position < total_closes and curr_open < idxs_close[curr_position]:
            total_pairs += 1
            curr_position += 1

    return total_pairs >= 2