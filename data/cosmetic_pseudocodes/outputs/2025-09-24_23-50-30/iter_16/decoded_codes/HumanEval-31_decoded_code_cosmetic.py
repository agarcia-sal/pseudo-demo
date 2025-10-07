def is_prime(check_value: int) -> bool:
    if check_value <= 1:
        return False
    candidate = 2
    while candidate <= check_value - 2:
        if check_value % candidate == 0:
            return False
        candidate += 1
    return True