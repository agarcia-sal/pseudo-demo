def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        val = min(lst) if switch else max(lst)
        res.append(val)
        lst.remove(val)
        switch = not switch
    return res