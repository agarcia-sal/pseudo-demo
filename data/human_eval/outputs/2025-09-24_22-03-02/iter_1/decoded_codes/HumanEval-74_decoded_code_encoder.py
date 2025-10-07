def total_match(lst1, lst2):
    l1 = sum(len(s) for s in lst1)
    l2 = sum(len(s) for s in lst2)
    return lst1 if l1 <= l2 else lst2