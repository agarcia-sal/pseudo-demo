def median(l: list):
    l = sorted(l)
    length = len(l)
    remainder = length % 2
    if remainder == 1:
        middle_index = length // 2
        return l[middle_index]
    else:
        left_index = (length // 2) - 1
        right_index = length // 2
        left_value = l[left_index]
        right_value = l[right_index]
        sum_ = left_value + right_value
        result = sum_ / 2.0
        return result