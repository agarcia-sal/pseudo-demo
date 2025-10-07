def is_prime(arg1: int) -> bool:
    if arg1 < 2:
        return False
    idx = 2
    while idx <= arg1 - 2:
        if arg1 % idx == 0:
            return False
        idx += 1
    return True