def strange_sort_list(lst) -> list:
    res = []
    switch = True
    while len(lst) > 0:
        current_value = min(lst) if switch else max(lst)
        res.append(current_value)
        lst.remove(current_value)
        switch = not switch
    return res