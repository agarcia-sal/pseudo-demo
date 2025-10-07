def median(l: list) -> float:
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return l[middle_index]
    else:
        middle_index_1 = (length // 2) - 1
        middle_index_2 = length // 2
        sum_value = l[middle_index_1] + l[middle_index_2]
        median_value = sum_value / 2.0
        return median_value