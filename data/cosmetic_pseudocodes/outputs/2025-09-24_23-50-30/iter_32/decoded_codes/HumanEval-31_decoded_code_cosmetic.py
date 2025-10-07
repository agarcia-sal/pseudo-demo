def is_prime(p0: int) -> bool:
    p1: int = 2
    while not (p0 < 2):
        if p1 > (p0 - 2):
            return True
        else:
            if p0 % p1 == 0:
                return False
        p1 += 1
    return False