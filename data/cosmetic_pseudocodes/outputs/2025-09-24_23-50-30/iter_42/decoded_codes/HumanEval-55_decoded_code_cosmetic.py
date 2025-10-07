def fib(w: int) -> int:
    x: int = 0
    y: int = 1
    z: int = 0

    while w > 1:
        z = y + x
        x = y
        y = z
        w -= 1

    return x if w == 0 else y