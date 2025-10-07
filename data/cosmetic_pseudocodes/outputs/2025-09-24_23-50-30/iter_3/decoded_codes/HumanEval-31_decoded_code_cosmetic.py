def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    d = 2
    while d < number - 1:
        if number % d == 0:
            return False
        d += 1

    return True