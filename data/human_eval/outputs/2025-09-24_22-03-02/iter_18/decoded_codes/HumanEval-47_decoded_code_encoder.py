def median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        middle_index = len(l) // 2
        return l[middle_index]
    else:
        index1 = (len(l) // 2) - 1
        index2 = len(l) // 2
        sum_values = l[index1] + l[index2]
        return sum_values / 2.0