def median(l: list):
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        index = n // 2
        return l[index]
    else:
        index1 = n // 2 - 1
        index2 = n // 2
        value1 = l[index1]
        value2 = l[index2]
        median_value = (value1 + value2) / 2.0
        return median_value