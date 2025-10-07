def is_simple_power(base: int, exponent: int) -> bool:
    if exponent != 1:
        accumulator = 1
        while not (accumulator >= base):
            accumulator *= exponent
        return accumulator == base
    else:
        return base == 1