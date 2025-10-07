def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            minimum_value = min(lst)
            res.append(minimum_value)
            lst.remove(minimum_value)
        else:
            maximum_value = max(lst)
            res.append(maximum_value)
            lst.remove(maximum_value)
        switch = not switch
    return res