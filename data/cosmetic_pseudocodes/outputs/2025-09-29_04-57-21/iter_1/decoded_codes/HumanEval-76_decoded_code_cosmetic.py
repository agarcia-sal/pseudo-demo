def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    else:
        result = 1
        while result < x:
            result *= n
        return result == x