def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        value = min(lst) if switch else max(lst)
        res.append(value)
        lst.remove(value)
        switch = not switch
    return res