def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        if switch:
            value = min(lst)
        else:
            value = max(lst)
        res.append(value)
        lst.remove(value)
        switch = not switch
    return res