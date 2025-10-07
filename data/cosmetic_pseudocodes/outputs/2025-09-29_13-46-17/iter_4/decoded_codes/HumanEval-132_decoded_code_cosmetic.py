from typing import List


def is_nested(string: str) -> bool:
    def helper_open_close_pairs(
        ops: List[int], cps: List[int], pos: int, cnt: int
    ) -> int:
        if not ops or pos >= len(cps):
            return cnt
        head, tail = ops[0], ops[1:]
        if head < cps[pos]:
            return helper_open_close_pairs(tail, cps, pos + 1, cnt + 1)
        else:
            return helper_open_close_pairs(tail, cps, pos, cnt)

    open_brackets: List[int] = []
    close_brackets: List[int] = []

    def split_brackets_at(i: int) -> None:
        if i >= len(string):
            return
        ch = string[i]
        if ch == '[':
            open_brackets.append(i)
        else:
            close_brackets.append(i)
        split_brackets_at(i + 1)

    split_brackets_at(0)

    def reverse_list(lst: List[int], idx: int, result: List[int]) -> List[int]:
        if idx < 0:
            return result
        return reverse_list(lst, idx - 1, result + [lst[idx]])

    reversed_close = reverse_list(close_brackets, len(close_brackets) - 1, [])

    total_pairs = helper_open_close_pairs(open_brackets, reversed_close, 0, 0)

    return total_pairs >= 2