def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            current_element = min(lst)
        else:
            current_element = max(lst)
        res.append(current_element)
        lst.remove(current_element)
        switch = not switch
    return res