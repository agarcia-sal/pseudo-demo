def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor_var = 2
    while divisor_var <= number - 2:
        if number % divisor_var == 0:
            return False
        divisor_var += 1
    return True