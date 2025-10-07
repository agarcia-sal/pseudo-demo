def fib(beta: int) -> int:
    if beta == 0:
        return 0
    if beta == 1:
        return 1
    return fib(beta - 1) + fib(beta - 2)