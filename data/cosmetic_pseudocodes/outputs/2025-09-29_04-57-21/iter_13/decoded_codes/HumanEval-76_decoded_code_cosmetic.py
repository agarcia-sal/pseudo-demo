def is_simple_power(x: int, n: int) -> bool:
    if n != 1:
        accumulated = 1
        while accumulated < x:
            accumulated *= n
        return accumulated == x
    else:
        return x == 1