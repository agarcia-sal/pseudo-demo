def x_or_y(n: int, x: int, y: int) -> int:
    if n == 1:
        return y
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return y
        divisor += 1
    return x