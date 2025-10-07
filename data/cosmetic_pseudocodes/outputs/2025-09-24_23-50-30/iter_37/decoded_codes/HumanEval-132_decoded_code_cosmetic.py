from typing import List


def is_nested(string: str) -> bool:
    acc_open: List[int] = []
    acc_close: List[int] = []

    for pos in range(len(string)):
        if string[pos] == '[':
            acc_open.append(pos)
        else:
            acc_close.append(pos)

    acc_close.reverse()

    idx_open: int = 0
    idx_close: int = 0
    matches: int = 0
    total_close: int = len(acc_close)

    while idx_open < len(acc_open):
        if idx_close < total_close and acc_open[idx_open] < acc_close[idx_close]:
            matches += 1
            idx_close += 1
        idx_open += 1

    return matches >= 2