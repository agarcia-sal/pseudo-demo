def total_match(list1, list2):
    length_sum1 = 0
    for string in list1:
        length_sum1 += len(string)

    length_sum2 = 0
    for string in list2:
        length_sum2 += len(string)

    if length_sum1 <= length_sum2:
        return list1
    else:
        return list2