def strange_sort_list(lst):
    res = []
    switch = True
    lst = lst[:]
    while lst:
        if switch:
            val = min(lst)
        else:
            val = max(lst)
        res.append(val)
        lst.remove(val)
        switch = not switch
    return res