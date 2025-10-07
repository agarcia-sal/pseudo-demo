def max_element(lst):
    m = lst[0]
    for e in lst:
        if e > m:
            m = e
    return m