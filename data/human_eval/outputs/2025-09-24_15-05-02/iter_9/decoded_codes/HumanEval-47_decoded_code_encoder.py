def median(list_l):
    sorted_l = sorted(list_l)
    n = len(sorted_l)
    if n % 2 == 1:
        return sorted_l[n // 2]
    else:
        mid_index = n // 2
        return (sorted_l[mid_index - 1] + sorted_l[mid_index]) / 2.0