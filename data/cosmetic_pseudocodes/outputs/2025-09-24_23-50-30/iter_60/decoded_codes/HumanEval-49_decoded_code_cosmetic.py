from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def recur_zq(wq: int, eq: int) -> int:
        if eq == 0:
            return wq
        else:
            return recur_zq(((wq * 2 + integer_p) % integer_p), eq - 1)
    return recur_zq(1, integer_n)