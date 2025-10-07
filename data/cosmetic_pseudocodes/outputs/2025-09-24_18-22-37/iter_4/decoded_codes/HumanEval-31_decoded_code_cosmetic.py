def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor_counter = 2
    while divisor_counter <= value - 2:
        if value % divisor_counter == 0:
            return False
        divisor_counter += 1
    return True