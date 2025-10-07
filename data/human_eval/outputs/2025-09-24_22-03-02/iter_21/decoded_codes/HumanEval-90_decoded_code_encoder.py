def next_smallest(lst):
    unique_lst = set(lst)
    sorted_lst = sorted(unique_lst)
    lst = sorted_lst
    if len(lst) < 2:
        return None
    else:
        return lst[1]