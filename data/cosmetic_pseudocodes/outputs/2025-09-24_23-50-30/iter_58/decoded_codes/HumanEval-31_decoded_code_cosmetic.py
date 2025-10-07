def is_prime(a1: int) -> bool:
    if a1 < 2:
        return False
    a2 = 2
    while a2 <= a1 - 2:
        if a1 % a2 == 0:
            return False
        a2 += 1
    return True