def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        if switch:
            value_to_remove = min(lst)
        else:
            value_to_remove = max(lst)
        res.append(value_to_remove)
        lst.remove(value_to_remove)
        switch = not switch
    return res