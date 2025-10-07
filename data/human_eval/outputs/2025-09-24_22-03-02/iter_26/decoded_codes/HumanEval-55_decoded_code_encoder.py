def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    value1 = fib(n - 1)
    value2 = fib(n - 2)
    result = value1 + value2
    return result