from typing import Callable

def count_upper(str_param: str) -> int:
    def recur(pos: int, tally: int) -> int:
        if pos >= len(str_param):
            return tally
        current_char = str_param[pos]
        tally += int(current_char in {"A", "E", "I", "O", "U"})
        return recur(pos + 2, tally)
    return recur(0, 0)