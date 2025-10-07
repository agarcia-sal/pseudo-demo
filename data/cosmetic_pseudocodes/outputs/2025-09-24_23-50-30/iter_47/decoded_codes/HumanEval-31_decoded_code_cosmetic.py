def is_prime(value: int) -> bool:
    if value < 2:
        return False

    for index in range(2, value - 1):
        if value % index == 0:
            return False

    return True