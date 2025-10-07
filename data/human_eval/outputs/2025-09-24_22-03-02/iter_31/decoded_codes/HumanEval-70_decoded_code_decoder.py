def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        current_value = min(lst) if switch else max(lst)
        res.append(current_value)
        lst.remove(current_value)
        switch = not switch
    return res