def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor_index = 2
    while divisor_index <= value - 2:
        if value % divisor_index == 0:
            return False
        divisor_index += 1
    return True