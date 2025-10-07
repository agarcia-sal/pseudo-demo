def fib(value: int) -> int:
    if value == 0:
        return 0
    if value == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, value + 1):
        a, b = b, a + b
    return b