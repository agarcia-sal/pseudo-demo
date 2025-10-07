def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        element = min(lst) if switch else max(lst)
        res.append(element)
        lst.remove(element)
        switch = not switch
    return res