def strange_sort_list(lst):
    lst = lst[:]
    result = []
    switch = True
    while lst:
        val = min(lst) if switch else max(lst)
        result.append(val)
        lst.remove(val)
        switch = not switch
    return result