def below_threshold(l: list, t: int) -> bool:
    for e in l:
        if e >= t:
            return False
    return True