def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    if x < 1 or n <= 0:
        return False
    power = 1
    while power < x:
        power *= n
    return power == x