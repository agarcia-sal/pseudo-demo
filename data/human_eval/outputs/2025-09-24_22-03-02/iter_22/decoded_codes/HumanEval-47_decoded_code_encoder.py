def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        index = len(l) // 2
        return l[index]
    else:
        mid1 = len(l) // 2 - 1
        mid2 = len(l) // 2
        sum = l[mid1] + l[mid2]
        return sum / 2.0