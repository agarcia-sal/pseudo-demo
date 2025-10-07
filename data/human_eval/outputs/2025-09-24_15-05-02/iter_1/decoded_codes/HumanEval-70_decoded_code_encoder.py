def strange_sort_list(lst):
    res, s = [], True
    while lst != []:
        x = min(lst) if s else max(lst)
        res.append(x)
        lst.remove(x)
        s = not s
    return res