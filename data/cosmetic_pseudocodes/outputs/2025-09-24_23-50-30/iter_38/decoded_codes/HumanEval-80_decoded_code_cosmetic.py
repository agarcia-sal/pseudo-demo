from typing import Union


def is_happy(str_arg: str) -> bool:
    if len(str_arg) < 3:
        return False
    for idx_var in range(len(str_arg) - 2):
        cond_a: bool = str_arg[idx_var] == str_arg[idx_var + 1]
        cond_b: bool = str_arg[idx_var + 1] == str_arg[idx_var + 2]
        cond_c: bool = str_arg[idx_var] == str_arg[idx_var + 2]
        if cond_a or cond_b or cond_c:
            return False
    return True