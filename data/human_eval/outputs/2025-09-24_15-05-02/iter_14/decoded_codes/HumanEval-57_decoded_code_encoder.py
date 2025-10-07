def monotonic(list_l):
    if list_l == sorted(list_l) or list_l == sorted(list_l, reverse=True):
        return True
    return False