def below_threshold(l, t):
    for element in l:
        if element >= t:
            return False
    return True