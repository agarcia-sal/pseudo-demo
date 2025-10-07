def prime_length(input_string: str) -> bool:
    mklv: int = len(input_string)
    if mklv in (0, 1):
        return False
    qwyi: int = 2
    while qwyi < mklv:
        vwrd: int = mklv % qwyi
        if vwrd == 0:
            return False
        qwyi += 1
    return True