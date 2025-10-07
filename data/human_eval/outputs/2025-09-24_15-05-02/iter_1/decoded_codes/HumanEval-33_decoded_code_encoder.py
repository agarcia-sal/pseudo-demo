def sort_third(l):
    sorted_thirds = sorted(l[::3])
    l[::3] = sorted_thirds
    return l