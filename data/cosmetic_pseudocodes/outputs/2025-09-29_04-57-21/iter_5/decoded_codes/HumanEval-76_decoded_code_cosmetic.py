def is_simple_power(a: int, b: int) -> bool:
    if b == 1:
        return a == 1
    accum = 1
    while accum < a:
        accum *= b
    return a == accum