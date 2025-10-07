def sort_third(l):
    l = l[:]
    indices = range(0, len(l), 3)
    sorted_elements = sorted(l[i] for i in indices)
    for i, val in zip(indices, sorted_elements):
        l[i] = val
    return l