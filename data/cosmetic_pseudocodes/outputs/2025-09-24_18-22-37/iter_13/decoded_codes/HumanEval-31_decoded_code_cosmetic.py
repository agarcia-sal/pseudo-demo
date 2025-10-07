def is_prime(input_val: int) -> bool:
    if input_val < 2:
        return False
    for check_val in range(2, input_val):
        if input_val % check_val == 0:
            return False
    return True