def max_element(l: list) -> int:
    m = l[0]
    for i in range(len(l)):
        e = l[i]
        if e > m:
            m = e
    return m