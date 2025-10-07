def is_prime(item: int) -> bool:
    if item < 2:
        return False
    for position in range(2, item - 1):
        if item % position == 0:
            return False
    return True