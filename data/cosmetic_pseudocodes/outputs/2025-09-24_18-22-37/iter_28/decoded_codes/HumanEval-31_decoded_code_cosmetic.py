def is_prime(value: int) -> bool:
    if value < 2:
        return False

    limit: int = value - 2
    idx: int = 2
    checking: bool = True

    while idx <= limit and checking:
        remainder: int = value % idx
        if remainder == 0:
            checking = False
        else:
            idx += 1

    return checking