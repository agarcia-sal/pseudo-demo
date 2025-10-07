def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        middle_index = len(l) // 2
        return l[middle_index]
    else:
        left_middle_index = len(l) // 2 - 1
        right_middle_index = len(l) // 2
        left_middle_value = l[left_middle_index]
        right_middle_value = l[right_middle_index]
        median_value = (left_middle_value + right_middle_value) / 2.0
        return median_value