def below_threshold(list_l, threshold_t):
    for e in list_l:
        if e >= threshold_t:
            return False
    return True