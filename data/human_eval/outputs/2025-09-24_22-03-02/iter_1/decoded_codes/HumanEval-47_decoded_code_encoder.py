def median(l):
    s = sorted(l)
    n = len(s)
    if n % 2 != 0:
        return s[n // 2]
    else:
        return (s[n // 2 - 1] + s[n // 2]) / 2