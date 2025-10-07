from typing import Callable

def count_upper(str_param: str) -> int:
    def helper(pos_acc: int, acc_val: int) -> int:
        if pos_acc >= len(str_param):
            return acc_val
        if str_param[pos_acc] in {'A', 'E', 'I', 'O', 'U'}:
            return helper(pos_acc + 2, acc_val + 1)
        return helper(pos_acc + 2, acc_val)
    return helper(0, 0)