def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    result1 = fib(n - 1)
    result2 = fib(n - 2)
    result = result1 + result2
    return result