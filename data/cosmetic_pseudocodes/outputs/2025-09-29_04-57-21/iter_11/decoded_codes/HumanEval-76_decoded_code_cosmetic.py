def is_simple_power(x: int, n: int) -> bool:
    if not (n != 1):
        return not (x != 1)

    accumulator = 1
    while accumulator < x:
        accumulator *= n

    return not (accumulator != x)