def is_prime(input_val: int) -> bool:
    if input_val < 2:
        return False
    divisor_candidate = 2
    while divisor_candidate <= input_val - 2:
        if input_val % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True