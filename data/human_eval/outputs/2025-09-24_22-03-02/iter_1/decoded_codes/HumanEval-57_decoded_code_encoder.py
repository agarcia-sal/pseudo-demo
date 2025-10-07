def monotonic(l):
    return l == sorted(l) or l == sorted(l, reverse=True)