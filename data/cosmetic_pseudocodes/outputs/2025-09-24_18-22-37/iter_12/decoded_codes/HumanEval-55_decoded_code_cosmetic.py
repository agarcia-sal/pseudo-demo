def fib(alpha: int) -> int:
    if alpha != 0:
        if alpha != 1:
            return fib(alpha - 1) + fib(alpha - 2)
        else:
            return 1
    else:
        return 0