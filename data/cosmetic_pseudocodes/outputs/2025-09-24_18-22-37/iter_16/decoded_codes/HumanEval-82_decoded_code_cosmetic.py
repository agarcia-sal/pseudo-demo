def prime_length(xyz_param: str) -> bool:
    p: int = len(xyz_param)
    if p == 0:
        return False
    if p == 1:
        return False

    q: int = 2
    while q < p:
        r: int = p % q
        if r == 0:
            return False
        q += 1

    return True