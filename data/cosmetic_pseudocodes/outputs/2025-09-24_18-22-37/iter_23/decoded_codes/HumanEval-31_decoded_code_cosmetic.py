def is_prime(sample: int) -> bool:
    if sample < 2:
        return False
    checker = 2
    stop_value = sample - 2
    while checker <= stop_value:
        remainder = sample % checker
        if remainder == 0:
            return False
        checker += 1
    return True