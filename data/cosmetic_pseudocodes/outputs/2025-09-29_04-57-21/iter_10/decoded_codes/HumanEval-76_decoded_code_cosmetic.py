def is_simple_power(x: int, n: int) -> bool:
    if n != 1:
        accumulator = 1
        while accumulator < x:
            accumulator *= n
        return accumulator == x
    return x == 1