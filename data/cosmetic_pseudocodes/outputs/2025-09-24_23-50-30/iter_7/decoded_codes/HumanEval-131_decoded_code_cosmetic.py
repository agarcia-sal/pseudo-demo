from typing import Callable

def digits(n: int) -> int:
    s = str(n)

    def process(index: int, acc_prod: int, acc_odd: int) -> int:
        if index >= len(s):
            return 0 if acc_odd == 0 else acc_prod
        val = int(s[index])
        if val % 2 != 0:
            return process(index + 1, acc_prod * val, acc_odd + 1)
        return process(index + 1, acc_prod, acc_odd)

    return process(0, 1, 0)