def prime_length(qwerty: str) -> bool:
    asdf: int = len(qwerty)
    if asdf == 0 or asdf == 1:
        return False
    zxcv: int = 2
    while zxcv < asdf:
        if asdf % zxcv == 0:
            return False
        zxcv += 1
    return True