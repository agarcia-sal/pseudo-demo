from typing import Callable


def count_upper(str_arg: str) -> int:
    def recur(accum: int, pos: int) -> int:
        if not (pos < len(str_arg)):
            return accum
        cond: bool = str_arg[pos] in {'A', 'E', 'I', 'O', 'U'}
        return recur(accum + (1 if cond else 0), pos + 2)

    return recur(0, 0)