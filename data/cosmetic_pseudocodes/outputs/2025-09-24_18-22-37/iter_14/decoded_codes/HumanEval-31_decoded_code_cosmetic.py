def is_prime(cipher: int) -> bool:
    if cipher < 2:
        return False
    for count in range(2, cipher - 1):
        if cipher % count == 0:
            return False
    return True