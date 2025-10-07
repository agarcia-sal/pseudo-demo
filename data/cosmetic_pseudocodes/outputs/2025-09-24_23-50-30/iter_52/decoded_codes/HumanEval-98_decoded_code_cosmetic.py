from typing import Callable

def count_upper(str_arg: str) -> int:
    def recur(idx: int, acc: int) -> int:
        if idx >= len(str_arg):
            return acc
        if str_arg[idx] in {'A', 'E', 'I', 'O', 'U'}:
            return recur(idx + 2, acc + 1)
        return recur(idx + 2, acc)
    return recur(0, 0)