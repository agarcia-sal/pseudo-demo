def total_match(lst1, lst2):
    l1 = 0
    for i in range(len(lst1)):
        st = lst1[i]
        l1 += len(st)
    l2 = 0
    for j in range(len(lst2)):
        st = lst2[j]
        l2 += len(st)
    if l1 <= l2:
        return lst1
    else:
        return lst2