def total_match(list1, list2):
    length1 = 0
    for string in list1:
        length1 += len(string)
    length2 = 0
    for string in list2:
        length2 += len(string)
    if length1 <= length2:
        return list1
    else:
        return list2