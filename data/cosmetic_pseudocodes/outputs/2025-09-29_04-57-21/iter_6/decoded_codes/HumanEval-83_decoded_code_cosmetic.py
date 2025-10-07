def starts_one_ends(length: int) -> int:
    if length == 1:
        return 1
    exponent = length - 2
    power = 1
    base = 10
    for _ in range(exponent):
        power *= base
    return 18 * power