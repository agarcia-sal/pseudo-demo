def median(l: list):
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return l[middle_index]
    else:
        middle_index1 = (length // 2) - 1
        middle_index2 = length // 2
        sum_value = l[middle_index1] + l[middle_index2]
        return sum_value / 2.0