def strange_sort_list(lst):
    res = []
    switch = True
    while lst:
        if switch:
            min_value = lst[0]
            index = 0
            for i in range(1, len(lst)):
                if lst[i] < min_value:
                    min_value = lst[i]
                    index = i
            res.append(min_value)
            lst.pop(index)
        else:
            max_value = lst[0]
            index = 0
            for i in range(1, len(lst)):
                if lst[i] > max_value:
                    max_value = lst[i]
                    index = i
            res.append(max_value)
            lst.pop(index)
        switch = not switch
    return res