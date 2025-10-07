def median(list_l):
    list_l = sorted(list_l)
    n = len(list_l)
    mid = n // 2
    if n % 2 == 1:
        return list_l[mid]
    else:
        return (list_l[mid - 1] + list_l[mid]) / 2.0