from typing import Callable

def modp(n_param: int, p_param: int) -> int:
    def recurse(counter_var: int, acc_var: int) -> int:
        if counter_var < n_param:
            return recurse(counter_var + 1, (acc_var << 1) % p_param)
        else:
            return acc_var
    return recurse(0, 1)