def below_threshold(l: list, t: int) -> bool:
    length_l = len(l)
    index = 0
    while index < length_l:
        e = l[index]
        if e >= t:
            return False
        index += 1
    return True