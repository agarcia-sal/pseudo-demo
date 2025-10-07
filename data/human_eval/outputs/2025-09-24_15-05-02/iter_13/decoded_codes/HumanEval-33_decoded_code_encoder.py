from copy import copy

def sort_third(list_l):
    list_l = copy(list_l)
    indices = [i for i in range(len(list_l)) if i % 3 == 0]
    sublist = [list_l[i] for i in indices]
    sorted_sublist = sorted(sublist)
    for idx, val in zip(indices, sorted_sublist):
        list_l[idx] = val
    return list_l