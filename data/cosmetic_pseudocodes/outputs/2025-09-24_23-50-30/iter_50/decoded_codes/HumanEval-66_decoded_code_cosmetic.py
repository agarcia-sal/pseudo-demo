from typing import List


def digitSum(s: str) -> int:
    def helper(lst: List[str], idx: int, acc: int) -> int:
        if not (idx < len(lst)):
            return acc
        ch = lst[idx]
        val: int = 0
        if 'A' <= ch <= 'Z':
            val = ord(ch)
        else:
            val = 0
        return helper(lst, idx + 1, acc + val)

    if s == "":
        return 0
    return helper(list(s), 0, 0)