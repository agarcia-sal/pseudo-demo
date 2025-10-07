def is_sorted(lst):
    return not any(lst.count(x) > 2 for x in lst) and all(lst[i-1] <= lst[i] for i in range(1, len(lst)))