def strange_sort_list(lst):
    res = []
    switch = True
    while len(lst) > 0:
        if switch:
            min_value = lst[0]
            for index in range(1, len(lst)):
                if lst[index] < min_value:
                    min_value = lst[index]
            res.append(min_value)
            value_to_remove = min_value
        else:
            max_value = lst[0]
            for index in range(1, len(lst)):
                if lst[index] > max_value:
                    max_value = lst[index]
            res.append(max_value)
            value_to_remove = max_value
        index_to_remove = 0
        while index_to_remove < len(lst):
            if lst[index_to_remove] == value_to_remove:
                lst.pop(index_to_remove)
                break
            index_to_remove += 1
        switch = not switch
    return res