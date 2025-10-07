def is_prime(xqv: int) -> bool:
    if xqv < 2:
        return False

    aqm = 2
    while aqm <= xqv - 2:
        jul = xqv % aqm
        if jul == 0:
            return False
        aqm += 1

    return True