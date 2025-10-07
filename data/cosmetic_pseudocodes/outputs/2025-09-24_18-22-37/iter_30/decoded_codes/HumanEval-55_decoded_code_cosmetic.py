def fib(q: int) -> int:
    if q == 0:
        return 0
    if q == 1:
        return 1
    u = q - 1
    v = q - 2
    s = fib(u)
    t = fib(v)
    return s + t