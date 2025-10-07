from typing import Union

def fib(param_m: int) -> int:
    if param_m == 0:
        return 0
    if param_m == 1:
        return 1
    seq = [0, 1]
    idx = 2
    while idx <= param_m:
        total = seq[idx - 2] + seq[idx - 1]
        seq.append(total)
        idx += 1
    return seq[param_m]