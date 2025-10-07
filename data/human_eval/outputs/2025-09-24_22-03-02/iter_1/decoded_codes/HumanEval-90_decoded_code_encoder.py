def next_smallest(lst):
    s = sorted(set(lst))
    return None if len(s) < 2 else s[1]