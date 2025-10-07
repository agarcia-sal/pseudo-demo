def total_match(lst1, lst2):
    l1 = 0
    for index_i in range(len(lst1)):
        st = lst1[index_i]
        l1 += len(st)
    l2 = 0
    for index_j in range(len(lst2)):
        st = lst2[index_j]
        l2 += len(st)
    if l1 <= l2:
        return lst1
    else:
        return lst2