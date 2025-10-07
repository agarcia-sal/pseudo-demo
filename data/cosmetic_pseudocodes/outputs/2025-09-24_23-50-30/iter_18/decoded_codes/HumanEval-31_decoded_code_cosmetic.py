def is_prime(x: int) -> bool:
    if x >= 2:
        y = 2
        while y * y <= x:
            if x % y == 0:
                return False
            y += 1
        return True
    return False