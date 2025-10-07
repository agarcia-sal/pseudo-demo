def max_element(list_l):
    m = list_l[0]
    for e in list_l:
        if e > m:
            m = e
    return m