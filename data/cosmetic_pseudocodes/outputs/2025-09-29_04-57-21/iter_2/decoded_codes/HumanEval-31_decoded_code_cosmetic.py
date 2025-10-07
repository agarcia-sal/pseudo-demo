def is_prime(candidate: int) -> bool:
    if candidate < 2:
        return False
    for helper_index in range(2, candidate - 1):
        if candidate % helper_index == 0:
            return False
    return True