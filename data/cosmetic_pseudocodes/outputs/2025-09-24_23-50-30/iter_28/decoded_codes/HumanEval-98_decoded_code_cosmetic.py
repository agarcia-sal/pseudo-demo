from typing import Callable

def count_upper(str_param: str) -> int:
    def recur_count(curr_pos: int, acc: int) -> int:
        if curr_pos >= len(str_param):
            return acc
        chr_tmp = str_param[curr_pos]
        acc_updated = acc + (1 if chr_tmp in {"A", "E", "I", "O", "U"} else 0)
        return recur_count(curr_pos + 2, acc_updated)
    return recur_count(0, 0)