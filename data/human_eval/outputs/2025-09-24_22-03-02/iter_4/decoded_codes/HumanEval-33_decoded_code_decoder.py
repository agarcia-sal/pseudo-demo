def sort_third(l):
    l = l[:]
    sublist = [l[i] for i in range(0, len(l), 3)]
    sorted_sublist = sorted(sublist)
    for idx, val in zip(range(0, len(l), 3), sorted_sublist):
        l[idx] = val
    return l