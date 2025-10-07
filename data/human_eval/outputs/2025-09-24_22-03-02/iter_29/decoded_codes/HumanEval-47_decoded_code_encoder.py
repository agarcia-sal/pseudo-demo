def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        middle_index = len(l) // 2
        return (l[middle_index - 1] + l[middle_index]) / 2.0