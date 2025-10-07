def fib(delta: int) -> int:
    if delta == 0:
        return 0
    if delta == 1:
        return 1
    val1 = fib(delta - 1)
    val2 = fib(delta - 2)
    return val1 + val2