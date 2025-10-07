def median(l: list):
    l_sorted = []
    l_length = 0
    for i in range(len(l)):
        l_sorted.append(l[i])
    l_sorted.sort()
    l = l_sorted
    l_length = len(l)
    l_mod_2 = l_length % 2
    if l_mod_2 == 1:
        middle_index = l_length // 2
        return l[middle_index]
    else:
        middle_low_index = (l_length // 2) - 1
        middle_high_index = (l_length // 2)
        middle_sum = l[middle_low_index] + l[middle_high_index]
        median_value = middle_sum / 2.0
        return median_value