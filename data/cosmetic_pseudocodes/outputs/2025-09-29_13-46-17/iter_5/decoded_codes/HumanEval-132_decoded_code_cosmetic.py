from typing import List


def is_nested(strg: str) -> bool:
    open_positions: List[int] = []
    close_positions: List[int] = []

    def traverse(i: int) -> None:
        if i >= len(strg):
            return
        if strg[i] == '[':
            open_positions.append(i)
        else:
            close_positions.append(i)
        traverse(i + 1)

    traverse(0)

    def reverse_list(lst: List[int], idx: int, endIdx: int) -> None:
        if idx >= endIdx:
            return
        lst[idx], lst[endIdx] = lst[endIdx], lst[idx]
        reverse_list(lst, idx + 1, endIdx - 1)

    reverse_list(close_positions, 0, len(close_positions) - 1)

    matched = 0
    pos = 0
    limit = len(close_positions)

    for op in open_positions:
        if not (pos >= limit or op >= close_positions[pos]):
            matched += 1
            pos += 1

    return matched >= 2