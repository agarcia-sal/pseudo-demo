def fib(lambda_: int) -> int:
    if not (lambda_ > 0):
        return 0
    if not (lambda_ > 1):
        return 1
    return fib(lambda_ - 1) + fib(lambda_ - 2)