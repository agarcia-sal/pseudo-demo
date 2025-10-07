def median(l: list):
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return l[middle_index]
    else:
        left_middle_index = (length // 2) - 1
        right_middle_index = length // 2
        left_value = l[left_middle_index]
        right_value = l[right_middle_index]
        sum_value = left_value + right_value
        average = sum_value / 2.0
        return average