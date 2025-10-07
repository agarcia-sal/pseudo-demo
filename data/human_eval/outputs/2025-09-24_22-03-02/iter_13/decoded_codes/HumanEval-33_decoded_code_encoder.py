def sort_third(l):
    l = list(l)
    l[::3] = sorted(l[::3])
    return l