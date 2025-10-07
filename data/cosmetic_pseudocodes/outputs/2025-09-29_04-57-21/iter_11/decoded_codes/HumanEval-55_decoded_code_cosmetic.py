def fib(count: int) -> int:
    if count == 0:
        return 0
    if count == 1:
        return 1
    return fib(count - 2) + fib(count - 1)