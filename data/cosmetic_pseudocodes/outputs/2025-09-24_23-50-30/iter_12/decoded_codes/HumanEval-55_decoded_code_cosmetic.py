def fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1

    a: int = 0
    b: int = 1
    c: int = 0
    i: int = 2

    while i <= num:
        c = a + b
        a = b
        b = c
        i += 1

    return c