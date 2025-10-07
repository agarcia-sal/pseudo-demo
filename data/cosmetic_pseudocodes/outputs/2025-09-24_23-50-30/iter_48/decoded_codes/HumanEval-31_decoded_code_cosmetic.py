def is_prime(value: int) -> bool:
    if value < 2:
        return False
    idx = 2
    while idx <= value - 2:
        if value % idx == 0:
            return False
        idx += 1
    return True