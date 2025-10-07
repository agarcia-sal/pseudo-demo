def is_prime(number: int) -> bool:
    if number < 2:
        return False
    candidate = 2
    while candidate <= number - 2:
        if number % candidate == 0:
            return False
        candidate += 1
    return True