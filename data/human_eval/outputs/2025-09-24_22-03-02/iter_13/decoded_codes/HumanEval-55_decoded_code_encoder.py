def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fib(n - 1)
    temp = fib(n - 2)
    return result + temp