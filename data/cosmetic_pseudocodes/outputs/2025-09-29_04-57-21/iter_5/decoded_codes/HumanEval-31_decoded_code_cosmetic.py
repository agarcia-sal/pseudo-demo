def is_prime(input_val: int) -> bool:
    if input_val < 2:
        return False
    for counter in range(2, input_val - 1):
        if input_val % counter == 0:
            return False
    return True