def is_prime(value: int) -> bool:
    if value < 2:
        return False
    index = 2
    while True:
        if index > value - 2:
            break
        if value % index == 0:
            return False
        index += 1
    return True