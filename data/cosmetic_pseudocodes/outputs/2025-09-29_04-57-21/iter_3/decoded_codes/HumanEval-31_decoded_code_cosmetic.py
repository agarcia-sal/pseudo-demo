def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for candidate_divisor in range(2, number - 1):
        if number % candidate_divisor == 0:
            return False

    return True