def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    checker = 2
    while checker <= value - 2:
        if value % checker == 0:
            return False
        checker += 1
    return True