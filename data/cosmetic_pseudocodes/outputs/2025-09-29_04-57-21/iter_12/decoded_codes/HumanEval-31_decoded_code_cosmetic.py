def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor <= number - 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True