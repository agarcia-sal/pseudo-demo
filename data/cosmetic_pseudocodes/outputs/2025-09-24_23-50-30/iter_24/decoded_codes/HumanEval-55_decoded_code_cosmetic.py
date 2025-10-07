from typing import Union

def fib(theta: int) -> int:
    if theta < 2:
        if theta != 0:
            return 1
        return 0
    sigma = theta - 1
    tau = theta - 2
    return fib(sigma) + fib(tau)