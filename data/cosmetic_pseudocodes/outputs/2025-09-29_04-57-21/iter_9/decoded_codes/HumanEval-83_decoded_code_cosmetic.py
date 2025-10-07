def starts_one_ends(size_k: int) -> int:
    if size_k == 1:
        return 1
    exponent_value = size_k - 2
    power_result = 1
    counter = 0
    while counter < exponent_value:
        power_result *= 10
        counter += 1
    return 18 * power_result