def fib(count: int) -> int:
    if count <= 0:
        return 0
    if count < 2:
        return 1
    firstPrev: int = fib(count - 1)
    secondPrev: int = fib(count - 2)
    return firstPrev + secondPrev