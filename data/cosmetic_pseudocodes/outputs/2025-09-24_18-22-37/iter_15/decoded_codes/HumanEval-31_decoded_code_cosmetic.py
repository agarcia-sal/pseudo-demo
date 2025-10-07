def is_prime(sigma: int) -> bool:
    if sigma < 2:
        return False
    delta = 2
    while delta <= sigma - 2:
        omega = sigma % delta
        if omega == 0:
            return False
        delta += 1
    return True