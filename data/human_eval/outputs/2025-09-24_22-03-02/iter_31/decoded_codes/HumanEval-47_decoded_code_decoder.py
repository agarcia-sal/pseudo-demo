def median(l: list):
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middleIndex = length // 2
        return l[middleIndex]
    else:
        middleIndex1 = (length // 2) - 1
        middleIndex2 = length // 2
        value1 = l[middleIndex1]
        value2 = l[middleIndex2]
        return (value1 + value2) / 2.0