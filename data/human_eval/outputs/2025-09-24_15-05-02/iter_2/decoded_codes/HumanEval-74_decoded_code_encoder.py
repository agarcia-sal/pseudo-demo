def total_match(lst1, lst2):
    l1 = 0
    for string in lst1:
        l1 += len(string)

    l2 = 0
    for string in lst2:
        l2 += len(string)

    if l1 <= l2:
        return lst1
    else:
        return lst2