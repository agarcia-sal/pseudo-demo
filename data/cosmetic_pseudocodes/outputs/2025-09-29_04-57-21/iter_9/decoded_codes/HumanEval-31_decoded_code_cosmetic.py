def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor_candidate = 2
    while divisor_candidate <= number - 2:
        if number % divisor_candidate == 0:
            return False
        divisor_candidate += 1

    return True