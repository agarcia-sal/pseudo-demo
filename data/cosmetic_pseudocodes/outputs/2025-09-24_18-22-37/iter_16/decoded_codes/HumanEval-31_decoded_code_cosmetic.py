def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor_var = 2
    while divisor_var <= value - 2:
        if value % divisor_var == 0:
            return False
        divisor_var += 1
    return True