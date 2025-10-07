def is_prime(qwerty: int) -> bool:
    if qwerty < 2:
        return False

    divisor_var = 2
    stop_limit = qwerty - 2

    while divisor_var <= stop_limit:
        if qwerty % divisor_var == 0:
            return False
        divisor_var += 1

    return True