def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        current_element = min(lst) if switch else max(lst)
        res.append(current_element)
        lst.remove(current_element)
        switch = not switch
    return res