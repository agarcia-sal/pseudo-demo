def is_simple_power(base: int, exponent: int) -> bool:
    if exponent == 1:
        return base == 1
    product = 1
    while product < base:
        product *= exponent
    return product == base