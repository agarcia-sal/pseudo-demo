def is_prime(qux: int) -> bool:
    if qux < 2:
        return False
    zyph = 2
    while zyph <= qux - 2:
        if qux % zyph == 0:
            return False
        zyph += 1
    return True