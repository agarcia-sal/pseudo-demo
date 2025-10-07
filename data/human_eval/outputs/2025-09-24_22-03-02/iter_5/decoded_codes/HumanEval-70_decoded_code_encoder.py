def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            value = min(lst)
        else:
            value = max(lst)
        res.append(value)
        lst.remove(value)
        switch = not switch
    return res