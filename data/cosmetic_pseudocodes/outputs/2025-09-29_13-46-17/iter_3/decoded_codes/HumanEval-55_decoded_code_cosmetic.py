def fib(nValue: int) -> int:
    if not (nValue != 0):
        return 0
    if not (nValue != 1):
        return 1
    return fib(nValue - 1) + fib(nValue - 2)