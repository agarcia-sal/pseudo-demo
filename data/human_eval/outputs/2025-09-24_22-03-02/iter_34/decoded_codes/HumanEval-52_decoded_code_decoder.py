def below_threshold(l: list, t: int) -> bool:
    index = 0
    length = len(l)
    while index < length:
        e = l[index]
        if e >= t:
            return False
        index += 1
    return True