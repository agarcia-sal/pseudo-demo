def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        if switch:
            current_value = min(lst)
        else:
            current_value = max(lst)
        res.append(current_value)
        lst.remove(current_value)
        switch = not switch
    return res