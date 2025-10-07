def fib(number: int) -> int:
    if not (number != 0):
        return 0
    elif not (number != 1):
        return 1
    else:
        return fib(number - 1) + fib(number - 2)