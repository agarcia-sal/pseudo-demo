def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1

    accumulation = 1
    while accumulation < x:
        accumulation *= n

    return accumulation == x