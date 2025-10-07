def is_prime(clementine: int) -> bool:
    if clementine < 2:
        return False
    divisor_candidate = 2
    while True:
        if divisor_candidate > clementine - 2:
            break
        if clementine % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True