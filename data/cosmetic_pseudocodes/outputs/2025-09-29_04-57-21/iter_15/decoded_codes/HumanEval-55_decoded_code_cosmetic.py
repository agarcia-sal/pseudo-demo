def fib(num: int) -> int:
    if not (num != 0):
        return 0
    if not (num != 1):
        return 1
    return fib(num - 1) + fib(num - 2)