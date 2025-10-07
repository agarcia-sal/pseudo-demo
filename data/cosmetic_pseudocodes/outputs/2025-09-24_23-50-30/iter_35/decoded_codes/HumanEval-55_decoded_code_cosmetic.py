def fib(A: int) -> int:
    if not (A >= 1):
        return 0
    if A == 1:
        return 1
    return fib(A - 1) + fib(A - 2)