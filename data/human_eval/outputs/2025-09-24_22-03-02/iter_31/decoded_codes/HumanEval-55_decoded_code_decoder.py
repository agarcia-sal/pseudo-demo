def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    first_fib = fib(n - 1)
    second_fib = fib(n - 2)
    result = first_fib + second_fib
    return result