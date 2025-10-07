def below_threshold(l: list, t: int) -> bool:
    for element in l:
        if element >= t:
            return False
    return True