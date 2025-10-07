def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            min_value = min(lst)
            res.append(min_value)
            lst.remove(min_value)
        else:
            max_value = max(lst)
            res.append(max_value)
            lst.remove(max_value)
        switch = not switch
    return res