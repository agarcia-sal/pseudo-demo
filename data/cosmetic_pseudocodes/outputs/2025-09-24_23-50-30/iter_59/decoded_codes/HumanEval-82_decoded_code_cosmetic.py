def prime_length(q: str) -> bool:
    w: int = len(q)
    if not (w > 1):
        return False
    e: int = 2
    while e < w:
        if w % e == 0:
            return False
        e += 1
    return True