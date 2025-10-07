def is_simple_power(x: int, n: int) -> bool:
    if n == 1:
        return x == 1
    accumulator = 1
    while True:
        if accumulator >= x:
            break
        accumulator *= n
    return accumulator == x