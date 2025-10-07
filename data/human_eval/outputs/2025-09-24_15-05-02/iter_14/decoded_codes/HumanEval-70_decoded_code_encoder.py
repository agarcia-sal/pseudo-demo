def strange_sort_list(list_of_integers):
    result = []
    switch = True
    while list_of_integers:
        if switch:
            value = min(list_of_integers)
        else:
            value = max(list_of_integers)
        result.append(value)
        list_of_integers.remove(value)
        switch = not switch
    return result